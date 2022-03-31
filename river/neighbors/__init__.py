"""Neighbors-based learning.

Also known as *lazy* methods. In these methods, generalisation of the training data is delayed
until a query is received.

"""
from .base_neighbors import BaseKNN, NearestNeighbors
from .knn_classifier import KNNClassifier
from .knn_regressor import KNNRegressor

__all__ = ["BaseKNN", "NearestNeighbors", "KNNClassifier", "KNNRegressor"]
