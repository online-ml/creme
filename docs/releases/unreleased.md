# Unreleased

## bandit

- Bandit policies now return a single arm when the `pull` method is called, instead of yielding or one more arms at a time. This is simpler to understand. We will move back to multi-armed pulls in the future.
- Added `bandit.Exp3`.
- `bandit.UCB` and `bandit.Exp3` have an extra `reward_scaler` parameter, which can be any object that inherits from `compose.TargetTransformRegressor`. This allows scaling rewards before updating arms.

## compose

- `compose.TransformerProduct` now correctly returns a `compose.TransformerUnion` when a transformer is added to it.
- Fixed `compose.TransformerProduct`'s `transform_many` behavior.
- `compose.TransformerUnion` and `compose.TransformerProduct` will now clone the provided estimators, so that shallow copies aren't shared in different places.

## model_selection

- Added `model_selection.BanditClassifier`, which is the classification equivalent to `bandit.BanditRegressor`. Both are methods to perform online model selection via a bandit policy.

## multioutput

- `metrics.multioutput.MacroAverage` and `metrics.multioutput.MicroAverage` now loop over the keys of `y_true` instead of `y_pred`. This ensures a `KeyError` is correctly raised if `y_pred` is missing an output that is present in `y_true`.

## preprocessing

- Added `preprocessing.TargetMinMaxScaler`, which operates the same as `preprocessing.TargetStandardScaler`, but instead uses min-max scaling.
