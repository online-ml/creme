import datetime
import json
import shelve
import sys

import torch
from sklearn.linear_model import SGDClassifier
from vowpalwabbit import pyvw

from river import (
    base,
    compat,
    drift,
    dummy,
    ensemble,
    evaluate,
    linear_model,
    metrics,
    naive_bayes,
    neighbors,
)
from river import neural_net as nn
from river import optim, preprocessing, rules, stats, tree


def run_track(models, track, benchmarks):
    print(track.name)
    if track.name in benchmarks:
        completed = set((cr["Dataset"], cr["Model"]) for cr in benchmarks[track.name])
    else:
        completed = set()

    for model_name, model in models.items():
        print(f"\t{model_name}")
        for dataset in track:
            data_name = dataset.__class__.__name__
            if (data_name, model_name) in completed:
                print(f"\t\t[skipped] {data_name}")
                continue
            # Get cached data from the shelf
            results = benchmarks[track.name]
            res = next(track.run(model, dataset, n_checkpoints=1))
            res["Dataset"] = data_name
            res["Model"] = model_name
            for k, v in res.items():
                if isinstance(v, metrics.base.Metric):
                    res[k] = v.get()
            res["Time"] = res["Time"] / datetime.timedelta(milliseconds=1)
            res.pop("Step")
            results.append(res)

            # Writes updated version to the shelf
            benchmarks[track.name] = results
            print(f"\t\t[done] {data_name}")


tracks = [
    evaluate.BinaryClassificationTrack(),
    evaluate.MultiClassClassificationTrack(),
    evaluate.RegressionTrack(),
]


class PyTorchLogReg(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.linear = torch.nn.Linear(n_features, 1)
        self.sigmoid = torch.nn.Sigmoid()
        torch.nn.init.constant_(self.linear.weight, 0)
        torch.nn.init.constant_(self.linear.bias, 0)

    def forward(self, x):
        return self.sigmoid(self.linear(x))


class PyTorchModel:
    def __init__(self, network_func, loss, optimizer_func):
        self.network_func = network_func
        self.loss = loss
        self.optimizer_func = optimizer_func

        self.network = None
        self.optimizer = None

    def learn_one(self, x, y):

        # We only know how many features a dataset contains at runtime
        if self.network is None:
            self.network = self.network_func(n_features=len(x))
            self.optimizer = self.optimizer_func(self.network.parameters())

        x = torch.FloatTensor(list(x.values()))
        y = torch.FloatTensor([y])

        y_pred = self.network(x)
        loss = self.loss(y_pred, y)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return self


class PyTorchBinaryClassifier(PyTorchModel, base.Classifier):
    def predict_proba_one(self, x):

        # We only know how many features a dataset contains at runtime
        if self.network is None:
            self.network = self.network_func(n_features=len(x))
            self.optimizer = self.optimizer_func(self.network.parameters())

        x = torch.FloatTensor(list(x.values()))
        p = self.network(x).item()
        return {True: p, False: 1.0 - p}


class VW2RiverBase:
    def __init__(self, *args, **kwargs):
        self.vw = pyvw.Workspace(*args, **kwargs)

    def _format_x(self, x):
        return " ".join(f"{k}:{v}" for k, v in x.items())


class VW2RiverClassifier(VW2RiverBase, base.Classifier):
    def learn_one(self, x, y):

        # Convert {False, True} to {-1, 1}
        y = int(y)
        y_vw = 2 * y - 1

        ex = self._format_x(x)
        ex = f"{y_vw} | {ex}"
        self.vw.learn(ex)
        return self

    def predict_proba_one(self, x):
        ex = "| " + self._format_x(x)
        y_pred = self.vw.predict(ex)
        return {True: y_pred, False: 1.0 - y_pred}


LEARNING_RATE = 0.005

models = {
    "Binary classification": {
        "Logistic regression": (
            preprocessing.StandardScaler()
            | linear_model.LogisticRegression(optimizer=optim.SGD(LEARNING_RATE))
        ),
        "ALMA": preprocessing.StandardScaler() | linear_model.ALMAClassifier(),
        "Stochastic Gradient Tree": tree.SGTClassifier(),
        "sklearn SGDClassifier": (
            preprocessing.StandardScaler()
            | compat.SKL2RiverClassifier(
                SGDClassifier(
                    loss="log_loss", learning_rate="constant", eta0=LEARNING_RATE, penalty="none"
                ),
                classes=[False, True],
            )
        ),
        "PyTorch logistic regression": (
            preprocessing.StandardScaler()
            | PyTorchBinaryClassifier(
                network_func=PyTorchLogReg,
                loss=torch.nn.BCELoss(),
                optimizer_func=lambda params: torch.optim.SGD(params, lr=LEARNING_RATE),
            )
        ),
        "Vowpal Wabbit logistic regression": VW2RiverClassifier(
            sgd=True,
            learning_rate=LEARNING_RATE,
            loss_function="logistic",
            link="logistic",
            adaptive=False,
            normalized=False,
            invariant=False,
            l2=0.0,
            l1=0.0,
            power_t=0,
            quiet=True,
        ),
    },
    "Multiclass classification": {
        "Naive Bayes": naive_bayes.GaussianNB(),
        "Hoeffding Tree": tree.HoeffdingTreeClassifier(),
        "Hoeffding Adaptive Tree": tree.HoeffdingAdaptiveTreeClassifier(seed=42),
        "Extremely Fast Decision Tree": tree.ExtremelyFastDecisionTreeClassifier(),
        "Adaptive Random Forest": ensemble.AdaptiveRandomForestClassifier(seed=42),
        "Streaming Random Patches": ensemble.SRPClassifier(),
        "k-Nearest Neighbors": preprocessing.StandardScaler()
        | neighbors.KNNClassifier(window_size=100),
        "ADWIN Bagging": ensemble.ADWINBaggingClassifier(tree.HoeffdingTreeClassifier(), seed=42),
        "AdaBoost": ensemble.AdaBoostClassifier(tree.HoeffdingTreeClassifier(), seed=42),
        "Bagging": ensemble.BaggingClassifier(tree.HoeffdingTreeClassifier(), seed=42),
        "Leveraging Bagging": ensemble.LeveragingBaggingClassifier(
            tree.HoeffdingTreeClassifier(), seed=42
        ),
        "Stacking": ensemble.StackingClassifier(
            [
                preprocessing.StandardScaler() | linear_model.SoftmaxRegression(),
                naive_bayes.GaussianNB(),
                tree.HoeffdingTreeClassifier(),
                preprocessing.StandardScaler() | neighbors.KNNClassifier(window_size=100),
            ],
            meta_classifier=ensemble.AdaptiveRandomForestClassifier(seed=42),
        ),
        "Voting": ensemble.VotingClassifier(
            [
                preprocessing.StandardScaler() | linear_model.SoftmaxRegression(),
                naive_bayes.GaussianNB(),
                tree.HoeffdingTreeClassifier(),
                preprocessing.StandardScaler() | neighbors.KNNClassifier(window_size=100),
            ]
        ),
        # Baseline
        "[baseline] Last Class": dummy.NoChangeClassifier(),
    },
    "Regression": {
        "Linear Regression": preprocessing.StandardScaler() | linear_model.LinearRegression(),
        "Linear Regression with l1 regularization": preprocessing.StandardScaler()
        | linear_model.LinearRegression(l1=1.0),
        "Linear Regression with l2 regularization": preprocessing.StandardScaler()
        | linear_model.LinearRegression(l2=1.0),
        "Passive-Aggressive Regressor, mode 1": preprocessing.StandardScaler()
        | linear_model.PARegressor(mode=1),
        "Passive-Aggressive Regressor, mode 2": preprocessing.StandardScaler()
        | linear_model.PARegressor(mode=2),
        "k-Nearest Neighbors": preprocessing.StandardScaler()
        | neighbors.KNNRegressor(window_size=100),
        "Hoeffding Tree": preprocessing.StandardScaler() | tree.HoeffdingAdaptiveTreeRegressor(),
        "Hoeffding Adaptive Tree": preprocessing.StandardScaler()
        | tree.HoeffdingAdaptiveTreeRegressor(seed=42),
        "Stochastic Gradient Tree": tree.SGTRegressor(),
        "Adaptive Random Forest": preprocessing.StandardScaler()
        | ensemble.AdaptiveRandomForestRegressor(seed=42),
        "Adaptive Model Rules": preprocessing.StandardScaler()
        | rules.AMRules(drift_detector=drift.ADWIN()),
        "Streaming Random Patches": preprocessing.StandardScaler() | ensemble.SRPRegressor(seed=42),
        "Exponentially Weighted Average": preprocessing.StandardScaler()
        | ensemble.EWARegressor(
            models=[
                linear_model.LinearRegression(),
                tree.HoeffdingAdaptiveTreeRegressor(),
                neighbors.KNNRegressor(window_size=100),
                rules.AMRules(),
            ],
        ),
        "Multi-layer Perceptron": preprocessing.StandardScaler()
        | nn.MLPRegressor(
            hidden_dims=(5,),
            activations=(
                nn.activations.ReLU,
                nn.activations.ReLU,
                nn.activations.Identity,
            ),
            optimizer=optim.SGD(1e-3),
            seed=42,
        ),
        # Baseline
        "[baseline] Mean predictor": dummy.StatisticRegressor(stats.Mean()),
    },
}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "force":
        benchmarks = shelve.open("results", flag="n")
    else:
        benchmarks = shelve.open("results", flag="c")

    # Every multiclass model can also handle binary classification
    models["Binary classification"].update(models["Multiclass classification"])
    details = {}

    for track in tracks:
        run_track(models=models[track.name], track=track, benchmarks=benchmarks)
        details[track.name] = {"Dataset": {}, "Model": {}}
        for dataset in track.datasets:
            details[track.name]["Dataset"][dataset.__class__.__name__] = repr(dataset)
        for model_name, model in models[track.name].items():
            details[track.name]["Model"][model_name] = repr(model)

    log = {}
    for track in tracks:
        log[track.name] = benchmarks[track.name]

    with open("results.json", "w") as f:
        json.dump(log, f, sort_keys=True, indent=4)

    # Close the shelf
    benchmarks.close()

    with open("details.json", "w") as f:
        json.dump(details, f, sort_keys=True, indent=4)
