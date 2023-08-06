from __future__ import annotations

import abc
import collections
import copy
import math
import random
import typing

import numpy as np

from river import base, metrics, stats
from river.drift import ADWIN
from river.tree.hoeffding_tree_classifier import HoeffdingTreeClassifier
from river.tree.nodes.arf_htc_nodes import (
    RandomLeafMajorityClass,
    RandomLeafNaiveBayes,
    RandomLeafNaiveBayesAdaptive,
)
from river.tree.nodes.arf_htr_nodes import RandomLeafAdaptive, RandomLeafMean, RandomLeafModel
from river.tree.splitter import Splitter
from river.utils.random import poisson


class BaseForest(base.Ensemble):
    _FEATURES_SQRT = "sqrt"
    _FEATURES_LOG2 = "log2"

    def __init__(
        self,
        n_models: int,
        max_features: bool | str | int,
        lambda_value: int,
        drift_detector: base.DriftDetector | None,
        warning_detector: base.DriftDetector | None,
        metric: metrics.base.MultiClassMetric,
        disable_weighted_vote,
        seed,
        sliding_window_max_size : int = 10,
        mass_control_size : int = 3,
        selection_threshold : int = 5,
        selection_threshold_option : str = 'mode',
    ):
        super().__init__([])  # type: ignore
        self.n_models = n_models
        self.max_features = max_features
        self.lambda_value = lambda_value
        self.metric = metric
        self.disable_weighted_vote = disable_weighted_vote
        self.drift_detector = drift_detector
        self.warning_detector = warning_detector
        self.seed = seed
        self._rng = random.Random(self.seed) 
        # Internal parameters
        self._n_samples_seen = 0
        self._base_member_class: ForestMemberClassifier | None = None

        #selection of classifiers parameters
        self.sliding_window_max_size = sliding_window_max_size
        self.mass_control_size = mass_control_size * self.n_models
        self.selection_threshold = selection_threshold
        self.selection_threshold_option = selection_threshold_option
        #selection of classifiers windows and variables
        self.mass = [0] * (self.sliding_window_max_size + 1)
        self.results = [0] * n_models
        self.mass_control : typing.List[int] = []
        self.classification_threshold = 0

    @property
    def _min_number_of_models(self):
        return 0

    @classmethod
    def _unit_test_params(cls):
        yield {"n_models": 3}

    def _unit_test_skips(self):
        return {"check_shuffle_features_no_impact"}

    def learn_one(self, x: dict, y: base.typing.Target, **kwargs):
        self._n_samples_seen += 1

        if len(self) == 0:
            self._init_ensemble(sorted(x.keys()))

        for i, model in enumerate(self):
            # Get prediction for instance
            y_pred = model.predict_one(x)

            # Update performance evaluator
            model.metric.update(y_true=y, y_pred=y_pred)

            k = poisson(rate=self.lambda_value, rng=self._rng)
            if k > 0:
                model.learn_one(x=x, y=y, sample_weight=k, n_samples_seen=self._n_samples_seen)

            #update metrics and sliding windows
            correctly_classifies = 1 if self.results[i] == y else 0
            model.right_pred += correctly_classifies
            model.sliding_window.append(correctly_classifies)
            if len(model.sliding_window) == self.sliding_window_max_size + 1:
                rmv = model.sliding_window.pop(0)
                model.right_pred -= rmv
            self.mass_control.append(model.right_pred)
            self.mass[model.right_pred] += 1
            
            if len(self.mass_control) == self.mass_control_size + 1:
                rmv = self.mass_control.pop(0)
                self.mass[rmv] -= 1

        #get classification threshold for dynamic selection in predict_proba_one
        if self.selection_threshold_option == 'fixed':
            n_voting_classifiers = 0
            for i in range(self.selection_threshold, len(self.mass)):
                n_voting_classifiers += self.mass[i]
            if n_voting_classifiers == 0:
                self.classification_threshold = 0
            else:
                self.classification_threshold = self.selection_threshold
        elif self.selection_threshold_option == 'mean':
            mean = 0.0
            total = 0
            for model in self:
                if model.right_pred >= self.selection_threshold:
                    mean += self.mass[i]
                    total += 1
            mean = mean / total if total != 0 else 0
            self.classification_threshold = int(mean) if self.classification_threshold > mean else self.selection_threshold
        else:
            most_recurrent = 0
            n_voting_classifiers = 0
            for i in range(self.selection_threshold, len(self.mass)):
                n_voting_classifiers += self.mass[i]
                if self.mass[i] >= most_recurrent:
                    self.classification_threshold = i
                    most_recurrent =  self.mass[i]

            if n_voting_classifiers == 0:
                self.classification_threshold = 0
            
        


        return self

    def _init_ensemble(self, features: list):
        self._set_max_features(len(features))

        self.data = [
            self._base_member_class(  # type: ignore
                index_original=i,
                model=self._new_base_model(),
                created_on=self._n_samples_seen,
                drift_detector=self.drift_detector,
                warning_detector=self.warning_detector,
                is_background_learner=False,
                metric=self.metric,
                sliding_window_max_size = self.sliding_window_max_size
            )
            for i in range(self.n_models)
        ]

    @abc.abstractmethod
    def _new_base_model(self):
        raise NotImplementedError

    def _set_max_features(self, n_features):
        if self.max_features == "sqrt":
            self.max_features = round(math.sqrt(n_features))
        elif self.max_features == "log2":
            self.max_features = round(math.log2(n_features))
        elif isinstance(self.max_features, int):
            # Consider 'max_features' features at each split.
            pass
        elif isinstance(self.max_features, float):
            # Consider 'max_features' as a percentage
            self.max_features = int(self.max_features * n_features)
        elif self.max_features is None:
            self.max_features = n_features
        else:
            raise AttributeError(
                f"Invalid max_features: {self.max_features}.\n"
                f"Valid options are: int [2, M], float (0., 1.],"
                f" {self._FEATURES_SQRT}, {self._FEATURES_LOG2}"
            )
        # Sanity checks
        # max_features is negative, use max_features + n
        if self.max_features < 0:
            self.max_features += n_features
        # max_features <= 0
        # (m can be negative if max_features is negative and abs(max_features) > n),
        # use max_features = 1
        if self.max_features <= 0:
            self.max_features = 1
        # max_features > n, then use n
        if self.max_features > n_features:
            self.max_features = n_features


class BaseTreeClassifier(HoeffdingTreeClassifier):
    """Adaptive Random Forest Hoeffding Tree Classifier.

    This is the base-estimator of the Adaptive Random Forest classifier.
    This variant of the Hoeffding Tree classifier includes the `max_features`
    parameter, which defines the number of randomly selected features to be
    considered at each split.

    """

    def __init__(
        self,
        max_features: int = 2,
        grace_period: int = 200,
        max_depth: int | None = None,
        split_criterion: str = "info_gain",
        delta: float = 1e-7,
        tau: float = 0.05,
        leaf_prediction: str = "nba",
        nb_threshold: int = 0,
        nominal_attributes: list | None = None,
        splitter: Splitter | None = None,
        binary_split: bool = False,
        min_branch_fraction: float = 0.01,
        max_share_to_split: float = 0.99,
        max_size: float = 100.0,
        memory_estimate_period: int = 1000000,
        stop_mem_management: bool = False,
        remove_poor_attrs: bool = False,
        merit_preprune: bool = True,
        rng: random.Random | None = None,
    ):
        super().__init__(
            grace_period=grace_period,
            max_depth=max_depth,
            split_criterion=split_criterion,
            delta=delta,
            tau=tau,
            leaf_prediction=leaf_prediction,
            nb_threshold=nb_threshold,
            nominal_attributes=nominal_attributes,
            splitter=splitter,
            binary_split=binary_split,
            min_branch_fraction=min_branch_fraction,
            max_share_to_split=max_share_to_split,
            max_size=max_size,
            memory_estimate_period=memory_estimate_period,
            stop_mem_management=stop_mem_management,
            remove_poor_attrs=remove_poor_attrs,
            merit_preprune=merit_preprune,
        )

        self.max_features = max_features
        self.rng = rng

    def _new_leaf(self, initial_stats=None, parent=None):
        if initial_stats is None:
            initial_stats = {}

        if parent is None:
            depth = 0
        else:
            depth = parent.depth + 1

        if self._leaf_prediction == self._MAJORITY_CLASS:
            return RandomLeafMajorityClass(
                initial_stats,
                depth,
                self.splitter,
                self.max_features,
                self.rng,
            )
        elif self._leaf_prediction == self._NAIVE_BAYES:
            return RandomLeafNaiveBayes(
                initial_stats,
                depth,
                self.splitter,
                self.max_features,
                self.rng,
            )
        else:  # NAIVE BAYES ADAPTIVE (default)
            return RandomLeafNaiveBayesAdaptive(
                initial_stats,
                depth,
                self.splitter,
                self.max_features,
                self.rng,
            )

    def new_instance(self):
        new_instance = self.clone()
        # Use existing rng to enforce a different model
        new_instance.rng = self.rng
        return new_instance




class MSTSARFClassifier(BaseForest, base.Classifier):
    """Adaptive Random Forest classifier with Mass-based Short Term Selection of Classifiers (MSTS) [^1].

    This algorithm tracks the mass function (like a histrogram) of right predictions from the ensemble base classifiers.
    A threshold based in a measure of central tendency determines which classifiers vote a certain instance or not.


    Parameters
    ----------
    n_models
        Number of trees in the ensemble.
    max_features
        Max number of attributes for each node split.<br/>
        - If `int`, then consider `max_features` at each split.<br/>
        - If `float`, then `max_features` is a percentage and
          `int(max_features * n_features)` features are considered per split.<br/>
        - If "sqrt", then `max_features=sqrt(n_features)`.<br/>
        - If "log2", then `max_features=log2(n_features)`.<br/>
        - If None, then ``max_features=n_features``.
    lambda_value
        The lambda value for bagging (lambda=6 corresponds to Leveraging Bagging).
    metric
        Metric used to track trees performance within the ensemble.
        Defaults to `metrics.Accuracy()`.
    disable_weighted_vote
        If `True`, disables the weighted vote prediction.
    drift_detector
        Drift Detection method. Set to None to disable Drift detection.
        Defaults to `drift.ADWIN(delta=0.001)`.
    warning_detector
        Warning Detection method. Set to None to disable warning detection.
        Defaults to `drift.ADWIN(delta=0.01)`.
    grace_period
        [*Tree parameter*] Number of instances a leaf should observe between
        split attempts.
    max_depth
        [*Tree parameter*] The maximum depth a tree can reach. If `None`, the
        tree will grow indefinitely.
    split_criterion
        [*Tree parameter*] Split criterion to use.<br/>
        - 'gini' - Gini<br/>
        - 'info_gain' - Information Gain<br/>
        - 'hellinger' - Hellinger Distance
    delta
        [*Tree parameter*] Allowed error in split decision, a value closer to 0
        takes longer to decide.
    tau
        [*Tree parameter*] Threshold below which a split will be forced to break
        ties.
    leaf_prediction
        [*Tree parameter*] Prediction mechanism used at leafs.<br/>
        - 'mc' - Majority Class<br/>
        - 'nb' - Naive Bayes<br/>
        - 'nba' - Naive Bayes Adaptive
    nb_threshold
        [*Tree parameter*] Number of instances a leaf should observe before
        allowing Naive Bayes.
    nominal_attributes
        [*Tree parameter*] List of Nominal attributes. If empty, then assume that
        all attributes are numerical.
    splitter
        [*Tree parameter*] The Splitter or Attribute Observer (AO) used to monitor the class
        statistics of numeric features and perform splits. Splitters are available in the
        `tree.splitter` module. Different splitters are available for classification and
        regression tasks. Classification and regression splitters can be distinguished by their
        property `is_target_class`. This is an advanced option. Special care must be taken when
        choosing different splitters. By default, `tree.splitter.GaussianSplitter` is used
        if `splitter` is `None`.
    binary_split
        [*Tree parameter*] If True, only allow binary splits.
    min_branch_fraction
        [*Tree parameter*] The minimum percentage of observed data required for branches
        resulting from split candidates. To validate a split candidate, at least two resulting
        branches must have a percentage of samples greater than `min_branch_fraction`. This
        criterion prevents unnecessary splits when the majority of instances are concentrated
        in a single branch.
    max_share_to_split
        [*Tree parameter*] Only perform a split in a leaf if the proportion of elements
        in the majority class is smaller than this parameter value. This parameter avoids
        performing splits when most of the data belongs to a single class.
    max_size
        [*Tree parameter*] Maximum memory (MB) consumed by the tree.
    memory_estimate_period
        [*Tree parameter*] Number of instances between memory consumption checks.
    stop_mem_management
        [*Tree parameter*] If True, stop growing as soon as memory limit is hit.
    remove_poor_attrs
        [*Tree parameter*] If True, disable poor attributes to reduce memory usage.
    merit_preprune
        [*Tree parameter*] If True, enable merit-based tree pre-pruning.
    sliding_window_max_size
        [*MSTS parameter*] size of the sliding window
        defaults to 10
    mass_control_size
        [*MSTS parameter*] the number of last instances the mass function will sum  
        defaults to 3
    selection_threshold
        [*MSTS parameter*] minimum threshold value for selection of classifiers
        defaults to 5
    selection_threshold_option
        [*MSTS parameter*] type of threshold to use<br/>
        -fixed<br/>
        -mean<br/>
        -mode<br/>
        defaults to mode
    seed
        Random seed for reproducibility.
    

    Examples
    --------
    >>> from river import datasets
    >>> from river import ensemble
    >>> from river import evaluate
    >>> from river import metrics
    >>> from river import forest

    >>> dataset = datasets.Elec2().take(3000)

    >>> native = forest.ARFClassifier(seed = 10)
    >>> msts = ensemble.MSTSARFClassifier(seed = 10)

    >>> native_acc = metrics.Accuracy()
    >>> msts_acc = metrics.Accuracy()

    >>> for (x,y) in dataset:

    ...    native_pred = native.predict_one(x)
    ...    msts_pred = msts.predict_one(x)

    ...    native_acc.update(y, native_pred)
    ...    msts_acc.update(y, msts_pred)

    ...    native.learn_one(x,y)
    ...    msts.learn_one(x,y)

    >>> print(f"Native ARF {native_acc}    MSTS ARF {msts_acc}")
    Native ARF Accuracy: 88.73%    MSTS ARF Accuracy: 90.07%

    References
    ----------
    [^1]: D. N. Assis, F. Enembreck and J. P. Barddal, "Mass-Based Short Term Selection of Classifiers in Data Streams", 
        2023 International Joint Conference on Neural Networks (IJCNN), Gold Coast, Australia, 2023, 
        pp. 1-8, doi: 10.1109/IJCNN54540.2023.10191423.
    """

    def __init__(
        self,
        n_models: int = 10,
        max_features: bool | str | int = "sqrt",
        lambda_value: int = 6,
        metric: metrics.base.MultiClassMetric | None = None,
        disable_weighted_vote=False,
        drift_detector: base.DriftDetector | None = None,
        warning_detector: base.DriftDetector | None = None,
        # Tree parameters
        grace_period: int = 50,
        max_depth: int | None = None,
        split_criterion: str = "info_gain",
        delta: float = 0.01,
        tau: float = 0.05,
        leaf_prediction: str = "nba",
        nb_threshold: int = 0,
        nominal_attributes: list | None = None,
        splitter: Splitter | None = None,
        binary_split: bool = False,
        min_branch_fraction: float = 0.01,
        max_share_to_split: float = 0.99,
        max_size: float = 100.0,
        memory_estimate_period: int = 2_000_000,
        stop_mem_management: bool = False,
        remove_poor_attrs: bool = False,
        merit_preprune: bool = True,
        sliding_window_max_size : int = 10,
        mass_control_size : int = 3,
        selection_threshold : int = 5,
        selection_threshold_option : str = 'mode',
        seed: int | None = None,
    ):
        super().__init__(
            n_models=n_models,
            max_features=max_features,
            lambda_value=lambda_value,
            metric=metric or metrics.Accuracy(),
            disable_weighted_vote=disable_weighted_vote,
            drift_detector=drift_detector or ADWIN(delta=0.001),
            warning_detector=warning_detector or ADWIN(delta=0.01),
            sliding_window_max_size = sliding_window_max_size,
            mass_control_size = mass_control_size,
            selection_threshold = selection_threshold,
            selection_threshold_option = selection_threshold_option,

            seed=seed,
        )

        self._n_samples_seen = 0
        self._base_member_class = ForestMemberClassifier  # type: ignore

        # Tree parameters
        self.grace_period = grace_period
        self.max_depth = max_depth
        self.split_criterion = split_criterion
        self.delta = delta
        self.tau = tau
        self.leaf_prediction = leaf_prediction
        self.nb_threshold = nb_threshold
        self.nominal_attributes = nominal_attributes
        self.splitter = splitter
        self.binary_split = binary_split
        self.min_branch_fraction = min_branch_fraction
        self.max_share_to_split = max_share_to_split
        self.max_size = max_size
        self.memory_estimate_period = memory_estimate_period
        self.stop_mem_management = stop_mem_management
        self.remove_poor_attrs = remove_poor_attrs
        self.merit_preprune = merit_preprune    
        

    @property
    def _mutable_attributes(self):
        return {
            "max_features",
            "lambda_value",
            "grace_period",
            "delta",
            "tau",
        }

    @property
    def _multiclass(self):
        return True

    def predict_proba_one(self, x: dict) -> dict[base.typing.ClfTarget, float]:
        y_pred: typing.Counter = collections.Counter()

        if len(self) == 0:
            self._init_ensemble(sorted(x.keys()))
            return y_pred  # type: ignore

        for i, model in enumerate(self):
            y_proba_temp = model.predict_proba_one(x)    
            self.results[i] =  max(y_proba_temp, key=y_proba_temp.get) if y_proba_temp else -1
            metric_value = model.metric.get()
            if not self.disable_weighted_vote and metric_value > 0.0:
                y_proba_temp = {k: val * metric_value for k, val in y_proba_temp.items()}
            
            #Select only classifiers that has the number of right predictions in the sliding window 
            # higher than the classification threshold extracted in learn_one 
            if model.right_pred >= self.classification_threshold:
                y_pred.update(y_proba_temp)

        total = sum(y_pred.values())
        if total > 0:
            return {label: proba / total for label, proba in y_pred.items()}
        return y_pred  # type: ignore

    def _new_base_model(self):
        return BaseTreeClassifier(
            max_features=self.max_features,
            grace_period=self.grace_period,
            split_criterion=self.split_criterion,
            delta=self.delta,
            tau=self.tau,
            leaf_prediction=self.leaf_prediction,
            nb_threshold=self.nb_threshold,
            nominal_attributes=self.nominal_attributes,
            splitter=self.splitter,
            max_depth=self.max_depth,
            binary_split=self.binary_split,
            min_branch_fraction=self.min_branch_fraction,
            max_share_to_split=self.max_share_to_split,
            max_size=self.max_size,
            memory_estimate_period=self.memory_estimate_period,
            stop_mem_management=self.stop_mem_management,
            remove_poor_attrs=self.remove_poor_attrs,
            merit_preprune=self.merit_preprune,
            rng=self._rng,
        )


class BaseForestMember:
    """Base forest member class.

    This class represents a tree member of the forest. It includes a
    base tree model, the background learner, drift detectors and performance
    tracking parameters.

    The main purpose of this class is to train the foreground model.
    Optionally, it monitors drift detection. Depending on the configuration,
    if drift is detected then the foreground model is reset or replaced by a
    background model.

    Parameters
    ----------
    index_original
        Tree index within the ensemble.
    model
        Tree learner.
    created_on
        Number of instances seen by the tree.
    drift_detector
        Drift Detection method.
    warning_detector
        Warning Detection method.
    is_background_learner
        True if the tree is a background learner.
    metric
        Metric to track performance.
    right_pred
        number of right predictions made by the learner in the sliding window
    sliding_window
        sliding window with binary values indicating right and wrong predictions
    """

    def __init__(
        self,
        index_original: int,
        model: BaseTreeClassifier,
        created_on: int,
        drift_detector: base.DriftDetector,
        warning_detector: base.DriftDetector,
        is_background_learner,
        metric: metrics.base.MultiClassMetric,
        sliding_window_max_size : int 
    ):
        self.index_original = index_original
        self.model = model
        self.created_on = created_on
        self.is_background_learner = is_background_learner
        self.metric = metric.clone()
        self.background_learner = None

        # Drift and warning detection
        self.last_drift_on = 0
        self.last_warning_on = 0
        self.n_drifts_detected = 0
        self.n_warnings_detected = 0

        #selection of classifiers parameters
        self.right_pred = 0
        self.sliding_window : typing.List[int] = []
        self.sliding_window_max_size = sliding_window_max_size

        # Initialize drift and warning detectors
        if drift_detector is not None:
            self._use_drift_detector = True
            self.drift_detector = drift_detector.clone()
        else:
            self._use_drift_detector = False
            self.drift_detector = None

        if warning_detector is not None:
            self._use_background_learner = True
            self.warning_detector = warning_detector.clone()
        else:
            self._use_background_learner = False
            self.warning_detector = None

    def reset(self, n_samples_seen):
        if self._use_background_learner and self.background_learner is not None:
            #Replace foreground model# with background model
            self.right_pred = self.background_learner.right_pred
            self.sliding_window = copy.deepcopy(self.background_learner.sliding_window)

            # Replace foreground model with background model
            self.model = self.background_learner.model
            self.warning_detector = self.background_learner.warning_detector
            self.drift_detector = self.background_learner.drift_detector
            self.metric = self.background_learner.metric
            self.created_on = self.background_learner.created_on
            self.background_learner = None
        else:
            # Reset model
            self.right_pred = 0
            self.sliding_window = []
            self.model = self.model.new_instance()
            self.metric = self.metric.clone()
            self.created_on = n_samples_seen
            self.drift_detector = self.drift_detector.clone()

    def learn_one(self, x: dict, y: base.typing.Target, *, sample_weight: int, n_samples_seen: int):
        self.model.learn_one(x, y, sample_weight=sample_weight)

        if self.background_learner:
            #selection of classifiers
            correctly_classifiers = 1 if self.background_learner.model.predict_one(x=x) == y else 0 
            self.background_learner.right_pred += correctly_classifiers
            self.background_learner.sliding_window.append(correctly_classifiers)
            #alterar para parametro 11
            if len(self.background_learner.sliding_window) == self.sliding_window_max_size:
                rmv = self.background_learner.sliding_window.pop(0)
                self.background_learner.right_pred -= rmv
            # Train the background learner
            self.background_learner.model.learn_one(x=x, y=y, sample_weight=sample_weight)
            

        if self._use_drift_detector and not self.is_background_learner:
            drift_detector_input = self._drift_detector_input(
                y_true=y, y_pred=self.model.predict_one(x)  # type: ignore
            )

            # Check for warning only if use_background_learner is set
            if self._use_background_learner:
                self.warning_detector.update(drift_detector_input)
                # Check if there was a (warning) change
                if self.warning_detector.drift_detected:
                    self.last_warning_on = n_samples_seen
                    self.n_warnings_detected += 1
                    # Create a new background learner object
                    self.background_learner = self.__class__(  # type: ignore
                        index_original=self.index_original,
                        model=self.model.new_instance(),
                        created_on=n_samples_seen,
                        drift_detector=self.drift_detector,
                        warning_detector=self.warning_detector,
                        is_background_learner=True,
                        metric=self.metric,
                        sliding_window_max_size = self.sliding_window_max_size
                    )
                    # Reset the warning detector for the current object
                    self.warning_detector = self.warning_detector.clone()

            # Update the drift detector
            self.drift_detector.update(drift_detector_input)

            # Check if there was a change
            if self.drift_detector.drift_detected:
                self.last_drift_on = n_samples_seen
                self.n_drifts_detected += 1
                self.reset(n_samples_seen)

    @abc.abstractmethod
    def _drift_detector_input(
        self,
        y_true: base.typing.ClfTarget | base.typing.RegTarget,
        y_pred: base.typing.ClfTarget | base.typing.RegTarget,
    ):
        raise NotImplementedError


class ForestMemberClassifier(BaseForestMember, base.Classifier):  # type: ignore
    """Forest member class for classification"""

    def __init__(
        self,
        index_original: int,
        model: BaseTreeClassifier,
        created_on: int,
        drift_detector: base.DriftDetector,
        warning_detector: base.DriftDetector,
        is_background_learner,
        metric: metrics.base.MultiClassMetric,
        sliding_window_max_size : int
    ):
        super().__init__(
            index_original=index_original,
            model=model,
            created_on=created_on,
            drift_detector=drift_detector,
            warning_detector=warning_detector,
            is_background_learner=is_background_learner,
            metric=metric,
            sliding_window_max_size = sliding_window_max_size
        )

    def _drift_detector_input(  # type: ignore
        self, y_true: base.typing.ClfTarget, y_pred: base.typing.ClfTarget
    ):
        return int(not y_true == y_pred)  # Not correctly_classifies

    def predict_one(self, x):
        return self.model.predict_one(x)

    def predict_proba_one(self, x):
        return self.model.predict_proba_one(x)


