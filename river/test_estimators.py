"""General tests that all estimators need to pass."""
import copy
import importlib
import inspect

import pytest

from river import (
    base,
    cluster,
    compose,
    ensemble,
    facto,
    feature_extraction,
    feature_selection,
    imblearn,
    linear_model,
    multiclass,
    naive_bayes,
    neural_net,
    preprocessing,
    reco,
    selection,
    stats,
    time_series,
    utils,
)

try:
    from river.compat.pytorch import PyTorch2RiverBase

    PYTORCH_INSTALLED = True
except ImportError:
    PYTORCH_INSTALLED = False
from river.compat.river_to_sklearn import River2SKLBase
from river.compat.sklearn_to_river import SKL2RiverBase


def iter_estimators():
    for submodule in importlib.import_module("river").__all__:
        if submodule == "synth":
            submodule = "datasets.synth"

        def is_estimator(obj):
            return inspect.isclass(obj) and issubclass(obj, base.Estimator)

        for _, obj in inspect.getmembers(
            importlib.import_module(f"river.{submodule}"), is_estimator
        ):
            yield obj


def iter_estimators_which_can_be_tested():

    ignored = (
        River2SKLBase,
        SKL2RiverBase,
        compose.FuncTransformer,
        compose.Grouper,
        compose.Pipeline,
        compose.TargetTransformRegressor,
        ensemble.AdaptiveRandomForestClassifier,
        ensemble.AdaptiveRandomForestRegressor,
        ensemble.StackingClassifier,
        facto.FFMClassifier,
        facto.FFMRegressor,
        facto.FMClassifier,
        facto.FMRegressor,
        facto.FwFMClassifier,
        facto.FwFMRegressor,
        facto.HOFMClassifier,
        facto.HOFMRegressor,
        feature_extraction.Agg,
        feature_extraction.TargetAgg,
        feature_extraction.Lagger,
        feature_extraction.TargetLagger,
        feature_selection.PoissonInclusion,
        neural_net.MLPRegressor,
        preprocessing.PreviousImputer,
        preprocessing.OneHotEncoder,
        preprocessing.StatImputer,
        reco.Baseline,
        reco.BiasedMF,
        reco.FunkMF,
        reco.RandomNormal,
        imblearn.RandomOverSampler,
        imblearn.RandomUnderSampler,
        imblearn.RandomSampler,
        selection.SuccessiveHalvingClassifier,
        selection.SuccessiveHalvingRegressor,
        time_series.HoltWinters,
        time_series.SNARIMAX,
    )

    if PYTORCH_INSTALLED:
        ignored = (*ignored, PyTorch2RiverBase)

    def can_be_tested(estimator):
        return not inspect.isabstract(estimator) and not issubclass(estimator, ignored)

    for estimator in filter(can_be_tested, iter_estimators()):
        yield estimator(**estimator._unit_test_params())


@pytest.mark.parametrize(
    "estimator, check",
    [
        pytest.param(estimator, check, id=f"{estimator}:{check.__name__}")
        for estimator in list(iter_estimators_which_can_be_tested())
        + [
            feature_extraction.TFIDF(),
            linear_model.LogisticRegression(),
            preprocessing.StandardScaler() | linear_model.LinearRegression(),
            preprocessing.StandardScaler() | linear_model.PAClassifier(),
            (
                preprocessing.StandardScaler()
                | preprocessing.TargetStandardScaler(
                    regressor=linear_model.LinearRegression(),
                )
            ),
            (
                preprocessing.StandardScaler()
                | multiclass.OneVsRestClassifier(linear_model.LogisticRegression())
            ),
            (
                preprocessing.StandardScaler()
                | multiclass.OneVsRestClassifier(linear_model.PAClassifier())
            ),
            naive_bayes.GaussianNB(),
            preprocessing.StandardScaler(),
            cluster.KMeans(n_clusters=5, seed=42),
            preprocessing.MinMaxScaler(),
            preprocessing.MinMaxScaler() + preprocessing.StandardScaler(),
            feature_extraction.PolynomialExtender(),
            (
                feature_extraction.PolynomialExtender()
                | preprocessing.StandardScaler()
                | linear_model.LinearRegression()
            ),
            feature_selection.VarianceThreshold(),
            feature_selection.SelectKBest(similarity=stats.PearsonCorr()),
        ]
        for check in utils.estimator_checks.yield_checks(estimator)
        if check.__name__ not in estimator._unit_test_skips()
    ],
)
def test_check_estimator(estimator, check):
    check(copy.deepcopy(estimator))
