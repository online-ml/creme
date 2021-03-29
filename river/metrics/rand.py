from river import metrics

from . import base

__all__ = ["AdjustedRand", "Rand"]


class Rand(base.MultiClassMetric):
    """Rand Index.

    The Rand Index [^1] [^2] is a measure of the similarity between two data clusterings.
    Given a set of elements `S` and two partitions of `S` to compare, `X` and `Y`,
    define the following:

    * a, the number of pairs of elements in `S` that are in the **same** subset in `X`
    and in the **same** subset in `Y`

    * b, the number of pairs of elements in `S` that are in the **different** subset in `X`
    and in **different** subsets in `Y`

    * c, the number of pairs of elements in `S` that are in the **same** subset in `X`
    and in **different** subsets in `Y`

    * d, the number of pairs of elements in `S` that are in the **different** subset in `X`
    and in the **same** subset in `Y`

    The Rand index, R, is

    $$
    R = \frac{a+b}{a+b+c+d} = \frac{a+b}{\frac{n(n-1)}{2}}.
    $$

    Parameters
    ----------
    cm
        This parameter allows sharing the same confusion
        matrix between multiple metrics. Sharing a confusion matrix reduces the amount of storage
        and computation time.

    Examples
    --------
    >>> from river import metrics

    >>> y_true = [1, 1, 2, 2, 3, 3]
    >>> y_pred = [1, 1, 1, 2, 2, 2]

    >>> metric = metrics.Rand()

    >>> for yt, yp in zip(y_true, y_pred):
    ...     print(metric.update(yt, yp).get())
    0.0
    1.0
    0.3333333333333333
    0.5
    0.6
    0.6666666666666666

    >>> metric
    Rand: 0.666667

    References
    ----------
    [^1]: Wikipedia contributors. (2021, January 13). Rand index.
          In Wikipedia, The Free Encyclopedia,
          from https://en.wikipedia.org/w/index.php?title=Rand_index&oldid=1000098911
    [^2]: W. M. Rand (1971). "Objective criteria for the evaluation of clustering methods".
          Journal of the American Statistical Association. American Statistical Association.
          66 (336): 846–850. arXiv:1704.01036. doi:10.2307/2284239. JSTOR 2284239.

    """

    def __init__(self, cm=None):
        super().__init__()

    def get(self):

        pair_confusion_matrix = metrics.PairConfusionMatrix(self.cm).get()

        true_positives = pair_confusion_matrix[1][1]
        true_negatives = pair_confusion_matrix[0][0]

        total_pairs = self.cm.n_samples * (self.cm.n_samples - 1) / 2

        try:
            return (true_positives + true_negatives) / total_pairs
        except ZeroDivisionError:
            return true_positives + true_negatives


class AdjustedRand(base.MultiClassMetric):
    """Adjusted Rand Index.

    The Adjusted Rand Index is the corrected-for-chance version of the Rand Index [^1] [^2].
    Such a correction for chance establishes a baseline by using the expected similarity
    of all pair-wise comparisions between clusterings specified by a random model.

    Traditionally, the Rand Index was corrected using the Permutation Model for Clustering.
    However, the premises of the permutation model are frequently violated; in many
    clustering scenarios, either the number of clusters or the size distribution of those
    clusters vary drastically. Variations of the adjusted Rand Index account for different
    models of random clusterings.

    Though the Rand Index may only yield a value between 0 and 1, the Adjusted Rand index
    can yield negative values if the index is less than the expected index.

    Parameters
    ----------
    cm
        This parameter allows sharing the same confusion
        matrix between multiple metrics. Sharing a confusion matrix reduces the amount of storage
        and computation time.

    Examples
    --------
    >>> from river import metrics

    >>> y_true = [1, 1, 2, 2, 3, 3]
    >>> y_pred = [1, 1, 1, 2, 2, 2]

    >>> metric = metrics.AdjustedRand()

    >>> for yt, yp in zip(y_true, y_pred):
    ...     print(metric.update(yt, yp).get())
    1.0
    1.0
    0.0
    0.0
    0.09090909090909091
    0.24242424242424243

    >>> metric
    AdjustedRand: 0.242424

    References
    ----------
    [^1]: Wikipedia contributors. (2021, January 13). Rand index.
          In Wikipedia, The Free Encyclopedia,
          from https://en.wikipedia.org/w/index.php?title=Rand_index&oldid=1000098911
    [^2]: W. M. Rand (1971). "Objective criteria for the evaluation of clustering methods".
          Journal of the American Statistical Association. American Statistical Association.
          66 (336): 846–850. arXiv:1704.01036. doi:10.2307/2284239. JSTOR 2284239.

    """

    def __init__(self, cm=None):
        super().__init__(cm)

    def get(self):

        pair_confusion_matrix = metrics.PairConfusionMatrix(self.cm).get()

        true_negatives, false_positives = pair_confusion_matrix[0].values()
        false_negatives, true_positives = pair_confusion_matrix[1].values()

        try:
            return (
                2.0
                * (true_positives * true_negatives - false_negatives * false_positives)
                / (
                    (true_positives + false_negatives)
                    * (false_negatives + true_negatives)
                    + (true_positives + false_positives)
                    * (false_positives + true_negatives)
                )
            )
        except ZeroDivisionError:
            return 1.0
