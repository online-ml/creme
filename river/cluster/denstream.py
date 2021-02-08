import math
import sys

from river import base
from river.cluster.denstream_microcluster import MicroCluster


class Denstream(base.Clusterer):
    """Denstream

    In order to propose a solution to the combination of requiremen ts, including limited memory,
    one-pass constraints, no assumption on the number of clusters, discorvery of cluster with
    arbitrary shape and ability to handle outliers, *Denstream*, a new approach for discorvering clusters
    in an evolving data stream is presented in [1]_.

    The dense micro-clusters (names core-micro-clusters) is introduced to summarise the clusters with
    arbitrary shape, while the potential core-micro-cluster and outlier micro-cluster structures are proposed
    to maintain and distinguish the potential clusters and outliers. A novel pruning strategy is designed
    based on these concepts, which guarantees the precision of the weights of the micro-clusters with limited
    memory.

    Parameters
    ----------
    decaying_factor
        Parameter that controls the importance of historical data to current cluster.

    core_weight_threshold
        Parameter to determine the threshold of outlier relative to core micro clusters.

    tolerance_factor
        Parameter to determine the threshold of outliers relative to core micro cluster. In a normal setting,
        this parameter is usuallly set within the range $[0,1]$.

    radius
        This parameter is passed onto the DBSCAN offline algorithm as the $`\epsilon`$ parameter
        when a clustering request arrives.

    Attributes
    ----------
    p_micro_clusters
        The p micro clusters that are generated by the algorithm. When a generating cluster request arrives,
        these o-micro-clusters will go through a variant of DBSCAN algorithm to determine the final clusters.

    o_micro_clusters
        The outlier buffer, separating the processing of the potential core-micro-cluster and outlier-micro-clusters.

    clusters
        A set of final clusters of type `MicroCluster`, which means that these cluster include all the required
        information, including number of points, creation time, weight, (weighted) linear sum, (weighted) square sum,
        center and radius.

    n_clusters
        Number of clusters generated by the algorithm.

    Examples
    ----------

    The following example uses the default parameters of the algorithm to test its functionality. It can easily be seen
    that the set of evolving points `X` are designed so that there can be a clear picture drawn on how the clusters can
    be generated.

    >>> from river import cluster
    >>> from river import stream

    >>> X = [
    ...     [1, 0.5], [1, 0.625], [1, 0.75], [1, 1.125], [1, 1.5], [1, 1.75],
    ...     [4, 1.5], [4, 2.25], [4, 2.5], [4, 3]
    ... ]

    >>> denstream_test = cluster.Denstream(decaying_factor = 0.25,
    ...                                    core_weight_threshold = 2,
    ...                                    tolerance_factor = 0.75,
    ...                                    radius = 0.5)

    >>> for i, (x, _) in enumerate(stream.iter_array(X)):
    ...     denstream_test = denstream_test.learn_one(x)

    >>> denstream_test.predict_one({0:1, 1:2})
    0

    >>> denstream_test.predict_one({0:5, 1:2})
    0

    >>> denstream_test.n_clusters
    1

    >>> denstream_test.centers
    {0: {0: 3.4071388850052444, 1: 2.1432902903628905}}

    References
    ----------
    .. [1] Feng et al (2006, pp 328-339). Density-Based Clustering over an Evolving Data Stream with Noise.
    In Proceedings of the Sixth SIAM International Conference on Data Mining, April 20-22, ,
     April 20–22, 2006, Bethesda, MD, USA.
    .. [2] Ester et al (1996). A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases
    with Noise. In KDD-96 Proceedings, AAAI.
    """

    def __init__(
        self,
        decaying_factor: float = 0.25,
        core_weight_threshold: float = 5,
        tolerance_factor: float = 0.5,
        radius: float = 2,
    ):
        super().__init__()
        self.time_stamp = -1
        self.o_micro_clusters = {}
        self.p_micro_clusters = {}
        self.initialized = False
        self.lmbd = decaying_factor
        self.mu = core_weight_threshold
        self.beta = tolerance_factor
        self.eps = radius

        "number of clusters generated by applying the variant of DBSCAN algorithm \
        on p micro cluster centers and their centers"
        self.n_clusters = 0
        self.clusters = {}
        self.centers = {}

    @property
    def _T_p(self):
        T_p = math.ceil(
            1 / self.lmbd * math.log(self.beta * self.mu / (self.beta * self.mu - 1))
        )
        return T_p

    @staticmethod
    def _distance(point_a, point_b):
        distance = 0.0
        for i in range(len(point_a)):
            d = point_a[i] - point_b[i]
            distance += d * d
        return math.sqrt(distance)

    def _find_closest_cluster_index(self, point, micro_clusters):
        """
        Find the closest cluster index for a point from a set of micro clusters
        """
        min_distance = sys.float_info.max
        closest_cluster_index = -1
        for i, micro_cluster in micro_clusters.items():
            distance = self._distance(micro_cluster.center, point)
            if distance < min_distance:
                min_distance = distance
                closest_cluster_index = i
        return closest_cluster_index

    def merge(self, point):
        """
        Algorithm to merge a new point `p` into existing micro clusters.

        **Algorithm 1**: Merging tasks

        * Try to merge `p` into its nearest p-micro-cluster `c_p`
        * If the new radius of $c_p \leq \epsilon$
            - Merge `p` into `c_p`
        * Else:
            * Try to merge `p` into its nearest o-micro-cluster `c_o`:
                * If the new radius of `c_o`, $r_o > beta * mu$ :
                    * Merge `p` into `c_o`
                    * If the new weight of `c_o`, $\omega > \beta * \mu$:
                        * Remove `c_o` from the outlier buffer and create a new p-micro-cluster by `c_o`
                * Else:
                    * Create a new o-micro-cluster by `p` and insert it into the outlier-buffer

        Parameters
        ----------
        point
            A dictionary of features

        """
        # Note: pmc is the abbreviation for p-micro-cluster,
        #       omc is the abbreviation for o-micro-cluster.

        # create a new micro cluster from point p
        mc_from_p = MicroCluster(
            x=point,
            timestamp=self.time_stamp,
            decaying_factor=self.lmbd,
            current_time=self.time_stamp,
        )

        if len(self.p_micro_clusters) != 0:
            # try to merge p into its nearest p-micro-cluster c_p
            closest_pmc_index = self._find_closest_cluster_index(
                point, self.p_micro_clusters
            )
            new_pmc = self.p_micro_clusters[closest_pmc_index]
            new_pmc.add(mc_from_p)
            if new_pmc.radius <= self.eps:
                # merge p into nearest c_p
                self.p_micro_clusters[closest_pmc_index].add(mc_from_p)
        elif len(self.o_micro_clusters) != 0:
            closest_omc_index = self._find_closest_cluster_index(
                point, self.o_micro_clusters
            )
            new_omc = self.o_micro_clusters[closest_omc_index]
            new_omc.add(mc_from_p)
            if new_omc.radius <= self.eps:
                # merge p into nearest c_0
                self.o_micro_clusters[closest_omc_index].add(mc_from_p)
                if (
                    self.o_micro_clusters[closest_omc_index].weight
                    > self.beta * self.mu
                ):
                    # remove c_o from outlier-buffer
                    self.o_micro_clusters.pop(closest_omc_index)
                    # add a new p_micro_cluster by c_o
                    self.p_micro_clusters[len(self.p_micro_clusters)] = new_omc
            else:
                # create a new o-micro-cluster by p and add it to o_micro_clusters
                self.o_micro_clusters[len(self.o_micro_clusters)] = mc_from_p

    def learn_one(self, x, sample_weight=None):
        """Incrementally trains the model.

        The tasks performed in `learn_one()` follows the steps described in **Algorithm 2**
        by Feng Cao et al, apart from the part when a generating cluster request arrives (which
        will later be handled by `predict_one()`.

        Training tasks:

        * Calculate
        $$
        T_p = \lceil \frac{1}{\lambda} \log \left( \frac{\beta \mu}{\beta \mu - } right) \rceil
        $$ ;

        * Get the next data point `p` at current time `t` from data stream `DS`;
        * Merging `p` using **Algorithm 1** (implemented within the function `merge()`);
        * If $t \pmod T_p \equiv 0$, **then**
            * **for each p-micro-cluster `c_p` **do**
                * **if** the weight of `c_p`, $\omega_p < \beta * \mu$ **then**:
                    * Delete `c_p`;
                **end if**
            **end for**

            * **for** each o-micro-cluster `c_o` **do**
                * Calculate
                $$
                xi = \frac{2^{-\lambda (t - t_0 + T_p)} - 1 }{2^{-\lambda T_p} - 1}
                $$

                * **if** the weight of `c_0`, $\omega_o < xi$ **then**:
                    * Delete `c_o`;
                **end if**
            **end for**
        **end if**

        Parameters
        ----------
        x
            The point that is passed through the function to be learned by the algorithm

        sample_weight
            Weight of the sample (point)

        Returns
        -------
        self

        """
        self.time_stamp += 1

        # initialize
        if not self.initialized:
            mc_from_x = MicroCluster(
                x=x,
                timestamp=self.time_stamp,
                decaying_factor=self.lmbd,
                current_time=self.time_stamp,
            )
            if mc_from_x.weight >= self.beta * self.mu:
                self.p_micro_clusters[0] = mc_from_x
            else:
                self.o_micro_clusters[0] = mc_from_x
            self.initialized = True
            return self

        # update current_time of all micro clusters
        for p_micro_cluster in self.p_micro_clusters.values():
            p_micro_cluster.current_time = self.time_stamp
        for o_micro_cluster in self.o_micro_clusters.values():
            o_micro_cluster.current_time = self.time_stamp

        # merge x
        self.merge(x)

        # run through if conditions
        if self.time_stamp % self._T_p == 0:
            for i, p_micro_cluster in list(self.p_micro_clusters.items()):
                if p_micro_cluster.weight < self.beta * self.mu:
                    # delete c_p
                    self.p_micro_clusters.pop(i)
            for j, o_micro_cluster in list(self.o_micro_clusters.items()):
                # calculate xi
                xi = (
                    2
                    ** (
                        -self.lmbd
                        * (self.time_stamp - o_micro_cluster.creation_time + self._T_p)
                    )
                    - 1
                ) / (2 ** (-self.lmbd * self._T_p) - 1)
                if o_micro_cluster.weight < xi:
                    # delete c_o
                    self.o_micro_clusters.pop(j)
        return self

    def _is_directly_density_reachable(self, c_p, c_q):
        """
        Check that two clusters `c_p` and `c_q` are directly density reachable by checking the following conditions
            * Two weights of two clusters have to be greater than $\mu$;
            * The distance of two cluster centers have to be smaller than $2\epsilon$, and apparently have to be smaller
            than the sum of two radius.
        """
        # if c_p is directly reachable from c_q, weight of c_q > mu, and vice versa.
        # for two clusters to be connected, they have to be density reachable from a third cluster. hence check
        # check weight of two clusters
        if c_p.weight > self.mu and c_q.weight > self.mu:
            # check distance of two clusters and compare with 2*eps
            if self._distance(c_p.center, c_q.center) < 2 * self.eps:
                # further check that the distance is smaller than sum of radius
                if self._distance(c_p.center, c_q.center) < c_p.radius + c_q.radius:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def _query_neighbor(self, cluster):
        """
        Implementation of the `RangeQuery` function to be used in the variant oof the DBSCAN
        algorithm for offline clustering.

        Parameters
        ----------
        cluster
            A cluster of type `MicroCluster`

        Returns
        -------
        neighbors
            A set of p-micro-cluster of the model that belongs to the neighborhood of the `cluster`
            that is passed through the function. This is a dictionary with the structure
            `{p-micro-cluster: None}`.

        """
        neighbors = {}
        # scan all clusters within self.p_micro_clusters
        for pmc in self.p_micro_clusters.values():
            # check density reachable and check that the cluster itself does not appear in neighbors
            if self._is_directly_density_reachable(cluster, pmc) and cluster != pmc:
                neighbors[pmc] = None
        return neighbors

    @staticmethod
    def _generate_clusters_from_labels(cluster_labels):
        """
        From a set of cluster labels in the form of {cluster: label}, generate centers withe respect to labels.
        These centers will later be the centers generated by the Denstream algorithm.
        """
        # initiate the set for final clusters
        clusters = {}

        # generate set of clusters with the same label with the structure {j: p-micro-cluster}
        for i in range(max(cluster_labels.values()) + 1):
            j = 0
            pmcs_with_label_i = {}
            for pmc, label in cluster_labels.items():
                if label == i:
                    pmcs_with_label_i[j] = pmc
                    j += 1

            # generate a final big cluster from clusters with the same label using the add function in MicroCluster
            cluster = pmcs_with_label_i[0]
            for m in range(1, len(pmcs_with_label_i)):
                cluster.add(pmcs_with_label_i[m])

            clusters[i] = cluster

        n_clusters = len(clusters)

        return n_clusters, clusters

    def predict_one(self, x, sample_weight=None):
        """Predict the cluster index for each sample

        `predict_one()` is used to handle the case when a clustering request arrives.

        When a clustering request arrives, a variant of DBSCAN algorithm is applied on the set of on-line
        maintained p-micro-clusters to get the final result of clustering. Each p-micro-cluster `c_p`
        is regarded as a virtual point localed at the center of `c_p` with weight $\omega`$.

        The variant of DBSCAN algorithm includes two parameters $\epsilon$ and $\mu$.
        We adopt the concept of density connectivity to determine the final cluster. That is, all the
        density-connected p-micro-clusters form a cluster.

        After new clusters of p-micro-clusters are generated, the label of the new point is obtained
        by assessing the nearest cluster center with respect to that specific point using the already implemented
        query function `_find_closest_cluster_index()`.

        Parameters
        ----------
        x
            A dictionary of n features

        sample_weight
            Instance weight

        Returns
        -------
        y
            Cluster label

        """
        # This function handles the case when a clustering request arrives.
        # implementation of the DBSCAN algorithm proposed by Ester et al.

        # initiate labels of p-micro-clusters to None
        labels = {pmc: None for pmc in self.p_micro_clusters.values()}
        # cluster counter; in this algorithm cluster labels start with 0
        c = -1

        for pmc in self.p_micro_clusters.values():
            # previously processed in inner loop
            if labels[pmc] is not None:
                continue
            pmc_neighbors = self._query_neighbor(pmc)
            # no label as noise, as there are no min points
            # next cluster label
            c += 1
            labels[pmc] = c
            # neighbors to expand has already been generated by query_neighbor
            # which means that pmc_neighbors is already a seed set
            seed_set = pmc_neighbors.copy()
            # process every point in seed set
            for neighbor in seed_set:
                # check previously proceeded points
                if labels[neighbor] is not None:
                    continue
                labels[neighbor] = c
                # find neighbors
                neighbor_neighbors = self._query_neighbor(neighbor)
                # add new neighbors to seed set
                # no need for density check, as there are no minPts
                for neighbor_neighbor in neighbor_neighbors.keys():
                    seed_set[neighbor_neighbor] = None

        self.n_clusters, self.clusters = self._generate_clusters_from_labels(labels)

        self.centers = {i: self.clusters[i].center for i in range(self.n_clusters)}

        y = self._find_closest_cluster_index(x, self.clusters)

        return y

    def learn_predict_one(self, x, sample_weight=None):
        """Equivalent to `denstream.learn_one(x).predict_one(x)`, but faster

        Parameters
        ----------
        x
            A dictionary of features

        sample_weight
            Instance weight

        Returns
        -------
        y
            Cluster label
        """

        self.learn_one(x, sample_weight)

        y = self.predict_one(x, sample_weight)

        return y
