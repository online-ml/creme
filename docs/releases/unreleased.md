# Unreleased

- Introducing the `bandit` module for running multi-armed bandits
- Introducing the `sketch` module with summarization tools and data sketches working in a streaming fashion!

## bandit

- Added `bandit.EpsilonGreedy`.
- Added `bandit.UCB`.
- Added `bandit.ThomsonSampling`.
- Added a `bandit.base` module.
- Added `bandit.envs.CandyCaneContest`, which implements the Gym interface.

## model_selection

- Added `model_selection.BanditRegressor`, which is a generic model selection method that works with any bandit policy.
- Removed `model_selection.EpsilonGreedyRegressor` due to the addition of `model_selection.BanditRegressor`.
- Removed `model_selection.UCBRegressor` due to the addition of `model_selection.BanditRegressor`.

## proba

- Added `proba.Beta`.
- Added a `sample` method to each distribution.
- Added a `mode` property to each distribution.
- Replaced the `pmf` and `pdf` methods with a `__call__` method.

## sketch

- Moved `misc.Histogram` to `sketch.Histogram`.
- Moved `stats.LossyCount` to `sketch.HeavyHitters` and update its API to better match `collections.Counter`.
- Added missing return `self` in `HeavyHitters`.
- Added the Count-Min Sketch (`sketch.Counter`) algorithm for approximate element counting.
- Added an implementation of Bloom filter (`sketch.Set`) to provide approximate set-like operations.
