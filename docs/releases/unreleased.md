# Unreleased

## base

- The `base` module is now fully type-annotated. Some type hints have changed, but this does not impact the behaviour of the code. For instance, the regression target is now indicated as a float instead of a Number.
- The `tags` and `more_tags` properties of `base.Estimator` are now both a set of strings.
