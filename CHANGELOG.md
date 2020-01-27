# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## 0.5.0 - Unreleased

See progress [here](https://github.com/creme-ml/creme/milestone/1).

### Added

- `metrics.ClassificationReport` to get a global performance overview on a classification task.
- There is now a `expand_param_grid` method in `model_selection` to generate a list of models from a grid of parameters.
- Each estimator now has a `_set_params(**new_params)` method for creating a new instance with the current parameters as well as new ones. This is practical for generating multiple instances of the same model with different hyperparameters. For the while this is a private method but it might become public.
- The `successive_halving` method can now be used to select hyperparameters.
- Moved `TargetModifierRegressor` and `BoxCoxTransformRegressor` to the newly created `meta` module.
- Added `PreviousImputer` to the `impute` module for replacing missing values with their previous value.
- Added the `TrumpApproval` dataset, which is a toy regression dataset.
- Added the `AMSGrad` optimizer to the `optim` module
- Added `RandomUnderSampler`, `RandomOverSampler`, and `RandomSampler` to the newly created `imblearn` module.
- Added `PyTorch2CremeRegressor` and to the `compat` module
- Added `PoissonRegression` to `linear_model`
- Added `Poisson` to `optim.losses`
- Added `MaliciousURL` to `datasets`
- Added `TimeRolling` to `metrics`
- Added `RBFSampler` to `preprocessing`

### Fixed

- The implementation of `ROCAUC` was incorrect. Using the trapezoidal rule instead of Simpson's rule seems to be more robust.

### Changed

- Renamed `CountVectorizer` to `BoW`
- Renamed `TFIDFVectorizer` to `TFIDF`
- The `online_score` and `online_qa_score` methods from the `model_selection` module have now been merged into a single method named `progressive_val_score`.
- Fixed a bug in `NesterovMomentum`.
- The `datasets` module has been overhauled. Each dataset is now a class (e.g. `fetch_electricity` has become `Elec2`).
- The `SKL2Creme` classes in `compat` now require `n_features` and a `batch_size` parameters for preemptive memory allocation (which allows doing mini-batching).

### Removed

- `metrics.PerClass`, it is recommended that you use `metrics.ClassificationReport` instead as it gives a better overview.


## [0.4.4](https://pypi.org/project/creme/0.4.4/) - 2019-11-11

This release was mainly made to provide access to wheels for Windows and MacOS.

### Added

- `SNARIMAX` to `time_series`. This is a generic model which encompasses time series models such as ARIMA and NARX.
- Introduced a `clip_gradient` parameter to `LinearRegression` and `LogisticRegression`. Gradient was already implemented, but the maximum absolute value can now be set by the user.
- `AdaBoostClassifier` to `ensemble`. This is the first implementation of boosting in `creme`.

### Changed

- `optim.schedulers.Optimal` produces results that are identical to scikit-learn's `SGDRegressor` and ``SGDClassifier`` when setting the `learning_rate` parameter to `'optimal'`
- The `intercept_lr` parameter of `LinearRegression` and `LogisticRegression` can now be passed an instance of `optim.schedulers.Scheduler` as well as a `float`.

### Fixed

- The `SMAPE` metric implementation was missing a multiplication by 2, and is now correct.

## [0.4.3](https://pypi.org/project/creme/0.4.3/) - 2019-10-27

### Added

- `fetch_credit_card` to `datasets`, which streams a highly imbalanced dataset of fraudulent credit card transactions
- The `utils` module now has a `math` submodule

### Fixed

- The `debug_one` method of `DecisionTreeClassifier` now works
- Model that inherit from `Wrapper` (which includes `RandomForestClassifier`) can now be correctly pickled

## [0.4.1](https://pypi.org/project/creme/0.4.1/) - 2019-10-23

### Added

- Metrics can now be composed using the `+` operator, which is useful for evaluating multiple metrics
- `LogisticRegression` and `LinearRegression` now have a `intercept_lr` parameter
- `KNeighborsRegressor` and `KNeighborsClassifier` to `neighbors`
- `fetch_kdd99_http`, `fetch_sms` and `fetch_trec07p` to `datasets`
- `AdaMax` to `optim`
- `Renamer` to `compose`
- `IQR` and `RollingIQR` to `stats`
- The `initializers` submodule has been added to the `optim` module, it can be used for initializing weights in weight-based models such as linear regression
- `shuffle` to `stream` for shuffling a data stream by maintaining a buffer of fixed width
- `Detrender` now has a `window_size` parameter for detrending with a rolling mean
- `Rolling` to `metrics`, which eliminates the need for one specific rolling implementation per metric
- Each metric can now be passed a `sample_weight` argument
- More metrics:
    - `WeightedF1`
    - `WeightedFBeta`
    - `WeightedPrecision`
    - `WeightedRecall`
- `RandomForestClassifier` to `tree`

### Modified

- Renamed `optim.VanillaSGD` to `optim.SGD`
- Fixed a bug where `utils.dot` could take longer than necessary
- Cythonized `stats.Mean` and `stats.Var`
- Cythonized all the loss functions in `optim`
- `CountVectorizer` and `TFIDFVectorizer` won't raise an error when being pickled anymore
- Tests are now much more extensive, thanks mostly to the newly added estimator tags
- `stream.iter_csv` now has `fraction` and `seed` parameters to sample rows, deterministically or not
- Renamed `stream.iter_numpy` to `stream.iter_array`
- The module `optim` has been reorganized into submodules; namely `schedulers`, `initializers`, and `losses`. The top-level now only contains optimizers. Some classes have renamed accordingly. See the documentation for details.
- `stream.iter_csv` can now read from `gzip` files

### Removed

- `HedgeBinaryClassifier` from `ensemble`, as it's performance was subpar
- `GroupRegressor` from `ensemble` as this should be a special case of `StackingRegressor`

## [0.3.0](https://pypi.org/project/creme/0.3.0/) - 2019-06-23

### Added

- `ClassifierChain` and `RegressorChain` to `multioutput`
- `Normalizer` to `preprocessing`
- `load_chick_weights` to `datasets`
- More metrics:
    - `FBeta`
    - `MacroFBeta`
    - `MicroFBeta`
    - `MultiFBeta`
    - `RollingFBeta`
    - `RollingMacroFBeta`
    - `RollingMicroFBeta`
    - `RollingMultiFBeta`
    - `Jaccard`
    - `RollingConfusionMatrix`
    - `RegressionMultiOutput`
    - `MCC`
    - `RollingMCC`
    - `ROCAUC`
- `Multinomial` to `proba`
- `HedgeRegressor` and `StackingBinaryClassifier` to `ensemble`
- `QuantileLoss` and `MiniBatcher` to `optim`
- `LDA` to `decomposition`

### Modified

- `stream.iter_sklearn` now receives an `sklearn.utils.Bunch` instead of a callable, the parameter `load_dataset` was thus renamed `dataset`
- Moved `SplitRegressor` from `compose` to `ensemble` and renamed it to `GroupRegressor`
- Renamed `F1Score` to `F1`
- Improved the performance of `HedgeClassifier`

### Removed

- `utils.Window` because using `collections.deque` directly is fine

## [0.2.0](https://pypi.org/project/creme/0.2.0/) - 2019-05-27

### Added

- `BernoulliNB` and `ComplementNB` to `naive_bayes`
- `DecisionTreeClassifier` to `tree`
- `SDFT` and `Skyline` to `utils`
- `AutoCorrelation` and `EWVariance` to `stats`
- Rolling metrics:
    - `RollingAccuracy`
    - `RollingCrossEntropy`
    - `RollingF1`
    - `RollingLogLoss`
    - `RollingMacroF1`
    - `RollingMacroPrecision`
    - `RollingMacroRecall`
    - `RollingMAE`
    - `RollingMicroF1`
    - `RollingMicroPrecision`
    - `RollingMicroRecall`
    - `RollingMSE`
    - `RollingPrecision`
    - `RollingRecall`
    - `RollingRMSE`
    - `RollingRMSLE`
    - `RollingSMAPE`
- `AdaBound` to `optim`
- `fetch_bikes` to `datasets`
- `simulate_qa` to `stream`
- `online_qa_score` to `model_selection`
- `Pipeline`'s now have a `debug_one(x)` method

### Modified

- `CountVectorizer` and `VectorizerMixin` can now be directly be fed `str`s instead of having to use a `dict`
- The `dist` module has been renamed to `proba` and is now public, for the moment it contains a single distribution called `Gaussian`
- Renamed the `window_size` parameter to `size` in `Window` and `SortedWindow`
- Rename `Variance` to `Var` and `RollingVariance` to `RollingVar`
- `Blacklister` and `Whitelister` now take variadic inputs, which means you don't have to provide a list
- `Agg` and `TargetAgg` can now aggregate on multiple attributes

### Removed

- `MondrianTreeClassifier` and `MondrianTreeRegressor` because their performance wasn't good enough

## [0.1.0](https://pypi.org/project/creme/0.1.0/) - 2019-05-08

### Added

- `Covariance`, `PearsonCorrelation`, and `SmoothMean` to `stats`
- `VarianceThreshold` and `SelectKBest` to `feature_selection`
- `metrics`:
    - `ConfusionMatrix`
    - `CrossEntropy`
    - `MacroF1`
    - `MacroPrecision`
    - `MacroRecall`
    - `MicroF1`
    - `MicroPrecision`
    - `MicroRecall`
- Each metric now has a `bigger_is_better` property to indicate if a high value is better than a low one or not
- `NoChangeClassifier`, `PriorClassifier`, and `StatisticRegressor` to `dummy`; these are now used in `check_estimator` to check that models are at least as good as "dumb" models
- `convert_sklearn_to_creme` to `compat`
- `Blacklister`, `Whitelister`, and `SplitRegressor` to `compose`
- `fetch_electricity` to `datasets`
- `OptimalLR` to `optim`
- `Differ` to `feature_extraction`
- `StatImputer` to `impute`
- `CrossEntropy` to `optim`
- `PAClassifier`, `PARegressor`, and `SoftmaxRegression` to `linear_model`
- `check_estimator`, `Histogram`, `SortedWindow`, and `Window` to `utils`

### Removed

- `Discarder` from `preprocessing`
- `CategoricalImputer` and `NumericImputer` from `impute`
- The `fit_predict_one`, `fit_predict_proba_one`, and `fit_transform_one` have been deprecated
- `TargetEncoder` from `feature_extraction`
- All the passive aggressive methods from `optim`
- The `optim` module has a slightly simpler API

### Modified

- Added `on` and `sparse` parameters to `preprocessing.OneHotEncoder`
- Renamed `GroupBy` to `Agg` and `TargetGroupBy` to `TargetAgg` to `Agg`
- `convert_creme_to_sklearn` now returns an `sklearn.pipeline.Pipeline` when given `creme.compose.Pipeline`
- `pipeline.draw()` now works properly for arbitrary amounts of nesting, including nested `FeatureUnion`s


## [0.0.3](https://pypi.org/project/creme/0.0.3/) - 2019-03-21

### Added

- `PolynomialExtender`, `Discarder`, and `FuncTransformer` to `preprocessing`
- `FMRegressor` to `linear_model`
- `metrics`:
    - `Accuracy`
    - `MAE`
    - `MSE`
    - `RMSE`
    - `RMSLE`
    - `SMAPE`
    - `Precision` (binary)
    - `Recall` (binary)
    - `F1` (binary)
- `CategoricalImputer` to `impute`
- `stats`:
    - `Mode`
    - `Quantile`
    - `RollingQuantile`
    - `Entropy`
    - `RollingMin`
    - `RollingMax`
    - `RollingMode`
    - `RollingSum`
    - `RollingPeakToPeak`
- `convert_creme_to_sklearn` to `compat`
- `SVD` to `reco`
- `BoxCoxTransformRegressor`, `TargetModifierRegressor` to `compose`
- `iter_csv` to `stream`
- `fetch_restaurants` and `load_airline` to `datasets`
- `GaussianNB` to `naive_bayes`
- `Multinomial` and `Normal` to `dist`
- `PassiveAggressiveI` and `PassiveAggressiveII` to `optim`
- `TargetGroupBy` to `feature_extraction`
- `MondrianTreeClassifier` and `MondrianTreeRegressor` to `tree`
- `BaggingRegressor` to `ensemble`

### Modified

- `model_selection.online_score` now accepts a `creme` metric instead of an `sklearn` metric; it also checks that the provided metric can be used with the accompanying model
- Calling `fit_one` now returns the calling instance, not the out-of-fold prediction/transform
- `fit_predict_one`, `fit_predict_proba_one`, and `fit_transform_one` are available to reproduce the previous behavior
- Binary classifiers now output a `dict` with probabilities for `False` and `True` when calling `predict_proba_one`, which solves the interface issues of having multi-class classifiers do binary classification

### Removed

- All the passive-aggressive estimators from `linear_model`

## [0.0.2](https://pypi.org/project/creme/0.0.2/) - 2019-02-13

### Added

- Passive-aggressive models to `linear_model`
- `HedgeClassifier` to `ensemble`
- `RandomDiscarder` to `feature_selection`
- `NUnique`, `Min`, `Max`, `PeakToPeak`, `Kurtosis`, `Skew`, `Sum`, `EWMean` to `stats`
- `AbsoluteLoss`, `HingeLoss`, `EpsilonInsensitiveHingeLoss` to `optim`
- `sklearn` wrappers to `compat`
- `TargetEncoder` to `feature_extraction`
- `NumericImputer` to `impute`

### Changed

- Made sure the running statistics produce the same results as `pandas`'s `rolling` method
