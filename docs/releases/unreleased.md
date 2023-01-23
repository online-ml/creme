# Unreleased

## active

- Created this module dedicated to online active learning.
- Added `active.EntropySampler`.

## base

- Fixed an issue where an estimator that has attribute a pipeline could not be cloned.
- Added a `base.DriftAndWarningDetector` to clarify the difference between drift detectors that have a `warning_detected` property and those that don't.
- Added `MultiLabelClassifier`.
- Added `MultiTargetRegressor`.
- Added `drift.BinaryDriftDetector`.
- Added `drift.BinaryDriftAndWarningDetector`.

## conf

- Introduced this new module to perform conformal predictions.
- Added a `conf.Interval` dataclass to represent predictive intervals.
- Added `conf.RegressionJackknife`.

## datasets

- Removed unnecessary Numpy usage in the `synth` submodule.
- Changed `np.random.RandomState` to `np.random.default_rng` where necessary.

## drift

- Added `drift.DriftRetrainingClassifier`.
- Renamed `drift.PeriodicTrigger` to `drift.DummyDriftDetector` to clarify it is a naive baseline.
- Created a `binary` submodule to organize all drift detectors which only apply to binary inputs.

## ensemble

- Added `ensemble.ADWINBoostingClassifier`.
- Added `ensemble.BOLEClassifier`.

## evaluate

- `evaluate.progressive_val_score` and `evaluate.iter_progressive_val_score` will now also produce a report once the last sample has been processed, in addition to every `print_every` steps.

## feature_extraction

- `feature_extraction.BagOfWords` now outputs a dictionary, and not a `collections.Counter`.

## forest

- Created this new module to host all models based on an ensemble of decision trees.
- Moved `ensemble.AdaptiveRandomForestClassifier` to `forest.ARFClassifier`.
- Moved `ensemble.AdaptiveRandomForestRegressor` to `forest.ARFRegressor`.
- Added `forest.AMFClassifier`.
- Added `forest.OXTRegressor`.

## linear_model

- Renamed `use_dist` to `with_dist` in `linear_model.BayesianLinearRegression`'s `predict_one` method.

## multiclass

- Added a `coding_method` method to `multiclass.OCC` to control how the codes are randomly generated.

## multioutput

- Added `MultiClassEncoder` to convert multi-label tasks into multi-class problems.

## preprocessing

- Renamed `alpha` to `fading_factor` in `preprocessing.AdaptiveStandardScaler`.

## rules

- Renamed `alpha` to `fading_factor` in `rules.AMRules`.

## sketch

- Renamed `alpha` to `fading_factor` in `sketch.HeavyHitters`.

## stats

- Renamed `alpha` to `fading_factor` in `stats.Entropy`.
- Renamed `alpha` to `fading_factor` in `stats.EWMean`.
- Renamed `alpha` to `fading_factor` in `stats.EWVar`.

## tree

- Remove `LabelCombinationHoeffdingTreeClassifier`. New code should use `multioutput.MulticlassEncoder` instead.

## utils

- Removed artifacts from the merger.
