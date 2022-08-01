import abc
import itertools

import numpy as np
import pandas as pd

from river import stats, utils


class SymmetricMatrix(abc.ABC):

    _fmt = ",.3f"

    @property
    @abc.abstractmethod
    def matrix(self):
        ...

    def __getitem__(self, key):
        """

        A covariance matrix is symmetric. For ease of use we make the __getitem__ method symmetric.

        """
        i, j = key
        try:
            return self.matrix[i, j]
        except KeyError:
            return self.matrix[j, i]

    def __repr__(self):

        names = sorted(set(i for i, _ in self.matrix))

        headers = [""] + list(map(str, names))
        columns = [headers[1:]]
        for col in names:
            column = []
            for row in names:
                try:
                    val = (
                        self[row, col].get()
                        if isinstance(self[row, col], stats.base.Statistic)
                        else self[row, col]
                    )
                    column.append(f"{val:{self._fmt}}")
                except KeyError:
                    column.append("")
            columns.append(column)

        return utils.pretty.print_table(headers, columns)


class EmpiricalCovariance(SymmetricMatrix):
    """Empirical covariance matrix.

    Parameters
    ----------
    ddof
        Delta Degrees of Freedom.

    Examples
    --------

    >>> import numpy as np
    >>> import pandas as pd
    >>> from river import covariance

    >>> np.random.seed(42)
    >>> X = pd.DataFrame(np.random.random((8, 3)), columns=["red", "green", "blue"])
    >>> X
            red     green      blue
    0  0.374540  0.950714  0.731994
    1  0.598658  0.156019  0.155995
    2  0.058084  0.866176  0.601115
    3  0.708073  0.020584  0.969910
    4  0.832443  0.212339  0.181825
    5  0.183405  0.304242  0.524756
    6  0.431945  0.291229  0.611853
    7  0.139494  0.292145  0.366362

    >>> cov = covariance.EmpiricalCovariance()
    >>> for x in X.to_dict(orient="records"):
    ...     cov = cov.update(x)
    >>> cov
            blue     green    red
     blue    0.076    0.020   -0.010
    green    0.020    0.113   -0.053
      red   -0.010   -0.053    0.079

    There is also an `update_many` method to process mini-batches. The results are identical.

    >>> cov = covariance.EmpiricalCovariance()
    >>> cov = cov.update_many(X)
    >>> cov
            blue     green    red
     blue    0.076    0.020   -0.010
    green    0.020    0.113   -0.053
      red   -0.010   -0.053    0.079

    The covariances are stored in a dictionary, meaning any one of them can be accessed as such:

    >>> cov["blue", "green"]
    Cov: 0.020292

    Diagonal entries are variances:

    >>> cov["blue", "blue"]
    Var: 0.076119

    """

    def __init__(self, ddof=1):
        self._cov = {}
        self.ddof = ddof

    @property
    def matrix(self):
        return self._cov

    def update(self, x: dict):
        """Update with a single sample.
        Parameters
        ----------
        x
            A sample.
        """

        for i, j in itertools.combinations(sorted(x), r=2):
            try:
                cov = self[i, j]
            except KeyError:
                self._cov[i, j] = stats.Cov(self.ddof)
                cov = self[i, j]
            cov.update(x[i], x[j])

        for i, xi in x.items():
            try:
                var = self[i, i]
            except KeyError:
                self._cov[i, i] = stats.Var(self.ddof)
                var = self[i, i]
            var.update(xi)

        return self

    def revert(self, x: dict):
        """Downdate with a single sample.

        Parameters
        ----------
        x
            A sample.

        """

        for i, j in itertools.combinations(sorted(x), r=2):
            self[i, j].revert(x[i], x[j])

        for i, xi in x.items():
            self[i, i].revert(x[i])

        return self

    def update_many(self, X: pd.DataFrame):
        """Update with a dataframe of samples.

        Parameters
        ----------
        X
            A dataframe of samples.

        """

        # dict -> numpy
        X_arr = X.values
        mean_arr = X_arr.mean(axis=0)
        cov_arr = np.cov(X_arr.T, ddof=self.ddof)

        mean = dict(zip(X.columns, mean_arr))
        cov = {
            (i, j): cov_arr[r, c]
            for (r, i), (c, j) in itertools.combinations_with_replacement(enumerate(X.columns), r=2)
        }

        for i, j in itertools.combinations(sorted(X.columns), r=2):
            try:
                self[i, j]
            except KeyError:
                self._cov[i, j] = stats.Cov(self.ddof)
            self._cov[i, j] += stats.Cov._from_state(
                n=len(X),
                mean_x=mean[i],
                mean_y=mean[j],
                cov=cov.get((i, j), cov.get((j, i))),
                ddof=self.ddof,
            )

        for i in X.columns:
            try:
                self[i, i]
            except KeyError:
                self._cov[i, i] = stats.Var(self.ddof)
            self._cov[i, i] += stats.Var._from_state(
                n=len(X), m=mean[i], sig=cov[i, i], ddof=self.ddof
            )

        return self
