# Unreleased

- Moved all the public modules imports from `river/__init__.py` to `river/api.py` and removed unnecessary dependencies between modules enabling faster cherry-pick imports times (≈ 3X).

## compat

- Moved the PyTorch wrappers to river-extra.

## compose

- Moved `utils.pure_inference_mode` to `compose.pure_inference_mode` and `utils.warm_up_mode` to `compose.warm_up_mode`.

## datasets

- Imports `synth`, enabling `from river import datasets; datasets.synth`.

## metrics

- Removed dependency to `optim`.

## utils

- Removed dependencies to `anomaly` and `compose`.
