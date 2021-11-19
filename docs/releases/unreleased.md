# Unreleased

- Wheels for Python 3.6 have been dropped.
- Wheels for Python 3.9 have been added.

## anomaly

- Moved `base.AnomalyDetector` to `anomaly.AnomalyDetector`.
- Implemented `anomaly.ConstantThresholder`.
- Implemented `anomaly.QuantileThresholder`.
- Implemented `anomaly.OneClassSVM`.

## base

- Renamed `base.WrapperMixin` to `base.Wrapper`.
- Introduced `base.WrapperEnsemble`.
- Clarified the difference between a `base.typing.Dataset` and a `base.typing.Stream`. A `Stream` is an instance of a `Dataset` and is stateful. A `Dataset` is stateless. It's essentially the same difference between an `Iterable` and an `Iterator` in the Python standard library.

## compat

- Added `compat.PyTorch2RiverClassifier`
- Implemented median absolute deviation in `stats.MAD`.
- Refactored `compat.PyTorch2RiverRegressor`
- Fixed an issue where some statistics could not be printed if they had not seen any data yet.

## compose

- You can now use a `list` as a shorthand to build a `TransformerUnion`.
- Fixed a visualization issue when using a pipeline with multiple feature unions.
- The prejudiced terms `blacklist` and `whitelist` have both been renamed to `keys`.
- Removed `learn_unsupervised` parameter from pipeline methods.
- Implemented `compose.TransformerProduct`.

## ensemble

- Bug fixes in `ensemble.SRPClassifier` and `ensemble.SRPRegressor`.
- Some estimators have been moved into the `ensemble` module.

## feature_extraction

- Implemented `feature_extraction.Lagger`.
- Implemented `feature_extraction.TargetLagger`.

## meta

This module has been deleted.

- Removed `meta.PredClipper`.
- Removed `meta.BoxCoxRegressor`.
- Moved `meta.TargetTransformRegressor` to `compose.TargetTransformRegressor`.
- Moved `meta.TargetStandardScaler` to `preprocessing.TargetStandardScaler`.

## optim

- `optim.Adam` and `optim.RMSProp` now work with `utils.VectorDict`s as well as `numpy.ndarray`s.
- Added `optim.losses.Huber`.

## selection

- This new module replaces the `expert` module.
- Implemented `selection.GreedyExpertRegressor`.

## stats

- Fixed an issue where some statistics could not be printed if they had not seen any data yet.
- Implemented median absolute deviation in `stats.MAD`.
- The `stats.Mean` and `stats.Var` implementations have been made more numerically stable.

## time_series

- `time_series.Detrender` and `time_series.GroupDetrender` have been removed as they overlap with `meta.TargetStandardScaler`.
- Implemented a `time_series.evaluate` method, which performs progressive validation for time series scenarios.
- Implemented `time_series.HorizonMetric` class to evaluate the performance of a forecasting model at each time step along a horizon.
- Implemented `time_series.HoltWinters`.

## utils

- Moved `model_selection.expand_param_grid` to `utils.expand_param_grid`.
- Added `utils.poisson`.
- Added the `utils.log_method_calls` context manager.
- Added the `utils.warm_up_mode` context manager.
- Added the `utils.pure_inference_model` context manager.
