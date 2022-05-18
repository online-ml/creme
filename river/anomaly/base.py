import abc

from river import base

__all__ = ["AnomalyDetector"]


class AnomalyDetector(base.Estimator):
    """An anomaly detector."""

    @property
    def _supervised(self):
        return False

    @abc.abstractmethod
    def learn_one(self, x: dict) -> "AnomalyDetector":
        """Update the model.

        Parameters
        ----------
        x
            A dictionary of features.

        Returns
        -------
        self

        """

    @abc.abstractmethod
    def score_one(self, x: dict) -> float:
        """Return an outlier score.

        A high score is indicative of an anomaly. A low score corresponds to a normal observation.

        Parameters
        ----------
        x
            A dictionary of features.

        Returns
        -------
        An anomaly score. A high score is indicative of an anomaly. A low score corresponds a
        normal observation.

        """


class SupervisedAnomalyDetector(base.Estimator):
    """A supervised anomaly detector."""

    @abc.abstractmethod
    def learn_one(self, x: dict, y: base.typing.Target) -> "SupervisedAnomalyDetector":
        """Update the model.

        Parameters
        ----------
        x
            A dictionary of features.

        Returns
        -------
        self

        """

    @abc.abstractmethod
    def score_one(self, x: dict, y: base.typing.Target) -> float:
        """Return an outlier score.

        A high score is indicative of an anomaly. A low score corresponds a normal observation.

        Parameters
        ----------
        x
            A dictionary of features.

        Returns
        -------
        An anomaly score. A high score is indicative of an anomaly. A low score corresponds a
        normal observation.

        """
