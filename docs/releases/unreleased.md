# Unreleased

## bandit

- Added `bandit.BayesUCB`.
- Added `bandit.evaluate_offline`, for evaluating bandits on historical (logged) data.

## compat

- The `predict_many` method scikit-learn models wrapped with `compat.convert_sklearn_to_river` raised an exception if the model had not been fitted on any data yet. Instead, default predictions will be produced, which is consistent with the rest of River.
- `compat.SKL2RiverRegressor` and `compat.SKL2RiverClassifier` didn't check whether features were ordered in the same way at each method call. They now store the list of feature names at the first function call, and align subsequent inputs in the same order.

## compose

- `compose.TransformerProduct` will now preserve the density of sparse columns.
- Added a `transform_many` method to `compose.FuncTransformer`, allowing it to be used in mini-batch pipelines.
- The `compose.pure_inference_mode` now works with mini-batching.

## neighbors

- Added `neighbors.SWINN` to power-up approximate nearest neighbor search. SWINN uses graphs to speed up nearest neighbor search in large sliding windows of data.
- Renamed `neighbors.NearestNeighbors` to `neighbors.LazySearch`.
- Standardize and create base classes for generic nearest neighbor search utilities.
- The user can now select the nearest neighbor search engine to use in `neighbors.KNNClassifier` and `neighbors.KNNRegressor`.

## preprocessing

- Rename `sparse` parameter to `drop_zeros` in `preprocessing.OneHotEncoder`.
- The `transform_many` method of `preprocessing.OneHotEncoder` will now return a sparse dataframe, rather than a dense one, which will consume much less memory.

## proba

- Added a `cdf` method to `proba.Beta`.

## tree

- Expose the `min_branch_fraction` parameter to avoid splits where most of the data goes to a single branch. Affects
classification trees.
- Added the `max_share_to_split` parameter to Hoeffding Tree classifiers. This parameters avoids splitting when the majority
class has most of the data.

## utils

- Fixed `utils.math.minkowski_distance`.
