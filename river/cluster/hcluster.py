from __future__ import annotations

from collections.abc import Callable

import numpy as np

from river import base, utils


# Node of a binary tree for Hierarchical Clustering
class BinaryTreeNode:
    def __init__(self, key: int, data: np.ndarray = None):
        self.data = data
        self.key = key
        # Children and parent
        self.left = None
        self.right = None
        self.parent = None


def euclidean_distance(w_i, w_j):
    # Euclidean distance between two nodes
    return np.linalg.norm(w_i.data - w_j.data)


class HierarchicalClustering(base.Clusterer):
    """Hierarchical Clustering.

    HierarchicalClustering is a stream hierarchical clustering algorithm. This algorithm [^1] inserts new nodes
    near the nodes it is similar to without breaking clusters of very similar nodes.

    Beginning with the whole tree `T`, it will compare the new node to this respective tree:
        * If `T` is just a leaf : merge
        * else if the nodes of T are more similar between them than with the new node: merge
        * else if the new node is more similar to the left subtree than to the right subtree:
          redo from the first point with T = left subtree
        * else (the new node is more similar to the right subtree than to the left subtree):
          redo from the first point with T = right subtree

    A certain window size can be chosen to use only the most recent points to make sure that the tree is not overloaded.

    Parameters
    ----------
    window_size
        number of data points to use
    distance_func
        distance function to use to compare the nodes

    Attributes
    ----------
    n
        number of nodes
    x_clusters
        data points used by the algorithm with the key of the node representing them

    References
    ----------
    [^1]: Anand Rajagopalan, Aditya Krishna Menon, Qin Cao, Gui Citovsky, Baris Sumengen and Sanjiv Kumar (2019). Online
    Hierarchical Clustering Approximations. arXiV:1909.09667. Available at: https://doi.org/10.48550/arXiv.1909.09667

    Examples
    --------

    The first example is with leaving the window size to 100. In the second one we put it at 2 to see how it works.

    >>> from river import cluster
    >>> from river import stream

    >>> X = [[1, 1, 1], [1, 1, 0], [20, 20, 20], [20, 20, 20.1], [0 , 1, 1]]

    >>> HC = cluster.HierarchicalClustering()

    >>> for x, _ in stream.iter_array(X):
    ...     HC = HC.learn_one(x)

    >>> HC.x_clusters
    {'[1 1 1]': 1, '[1 1 0]': 2, '[20 20 20]': 4, '[20.  20.  20.1]': 6, '[0 1 1]': 8}

    >>> HC.n
    9

    >>> print(HC)
            -> 6
        -> 7
            -> 4
    -> 5
            -> 8
        -> 9
                -> 2
            -> 3
                -> 1
    Printed Hierarchical Clustering Tree.

    >>> HC.get_all_clusters()
    [(1, [array([1, 1, 1])]), (2, [array([1, 1, 0])]), (4, [array([20, 20, 20])]), (6, [array([20. , 20. , 20.1])]), (8, [array([0, 1, 1])]), (3, [1, 2]), (5, [9, 7]), (7, [4, 6]), (9, [3, 8])]

    >>> HC.get_clusters_by_point()
    {'[1 1 1]': [1, 3, 9, 5], '[1 1 0]': [2, 3, 9, 5], '[20 20 20]': [4, 7, 5], '[20.  20.  20.1]': [6, 7, 5], '[0 1 1]': [8, 9, 5]}

    >>> HC.predict_one({0 : 20.1, 1 : 20, 2 : 20 })
    ([10, 11, 5], 7)

    >>> HC = HC.learn_one({0 : 20.1, 1 : 20, 2 : 20 })

    >>> print(HC)
            -> 10
        -> 11
                -> 6
            -> 7
                -> 4
    -> 5
            -> 8
        -> 9
                -> 2
            -> 3
                -> 1
    Printed Hierarchical Clustering Tree.

    >>> HC = cluster.HierarchicalClustering(window_size=2)

    >>> for x, _ in stream.iter_array(X):
    ...     HC = HC.learn_one(x)

    >>> HC.x_clusters
    {'[20.  20.  20.1]': 2, '[0 1 1]': 1}

    >>> HC.n
    3

    >>> print(HC)
        -> 2
    -> 3
        -> 1
    Printed Hierarchical Clustering Tree.
    """

    def __init__(
        self,
        window_size: int = 100,
        distance_func: Callable[[BinaryTreeNode, BinaryTreeNode], float] = None,
    ):
        # Number of nodes
        self.n = 0
        # Max number of leaves
        self.window_size = window_size
        # Dict : x data (str(array of size m)) -> key of the node
        self.x_clusters: dict[str, int] = {}
        # Dict : key -> node
        self.nodes: dict[int, BinaryTreeNode] = {}
        # First node of the tree
        self.root = None
        # Distance function
        self.distance = distance_func if distance_func is not None else euclidean_distance

    def otd_clustering(self, tree, x):
        # Online top down clustering (OTD), the first algorithm for online hierarchical clustering.
        # The algorithm performs highly efficient online updates and provably approximates Moseley-Wang revenue.
        x_string = np.array2string(x)
        if self.n == 1:
            # First node in the tree
            self.root = self.nodes[1]
        elif tree.data is not None:
            # If T is a leaf, we merge the two nodes together
            self.merge_nodes(tree, self.nodes[self.x_clusters[x_string]])
        elif tree.left is None:
            # If there is no node at the left of the intermediate node, we add it there
            tree.left = self.nodes[self.x_clusters[x_string]]
            self.nodes[self.x_clusters[x_string]].parent = tree
        elif tree.right is None:
            # If there is no node at the right of the intermediate node, we add it there
            tree.right = self.nodes[self.x_clusters[x_string]]
            self.nodes[self.x_clusters[x_string]].parent = tree
        elif self.intra_subtree_similarity(tree) < self.inter_subtree_similarity(
            tree, self.nodes[self.x_clusters[x_string]]
        ):
            # If the nodes in T are closer between them than with the new node, we merge T and the new node
            self.merge_nodes(tree, self.nodes[self.x_clusters[x_string]])
        elif self.inter_subtree_similarity(
            tree.left, self.nodes[self.x_clusters[x_string]]
        ) > self.inter_subtree_similarity(tree.right, self.nodes[self.x_clusters[x_string]]):
            # Continue to search where to merge the new node in the right part of T
            self.otd_clustering(tree.right, x)
        else:
            # Continue to search where to merge the new node in the left part of T
            self.otd_clustering(tree.left, x)

    def merge_nodes(self, tree, added_node):
        # Merge a new node (added node) to the tree
        # We create the node that will be the parent of the tree and the added node
        self.n += 1
        new_node = BinaryTreeNode(self.n)
        # We add the tree and the added node as its children
        new_node.left = tree
        new_node.right = added_node
        # The parent of the new node is the parent of the tree
        new_node.parent = tree.parent
        # If the tree is not the root, we set the child of its parent as new node (instead of T)
        if tree.parent is not None:
            if tree.parent.left.key == tree.key:
                tree.parent.left = new_node
            else:
                tree.parent.right = new_node
        # We add the new node as the parent of the tree and the added node
        tree.parent = new_node
        added_node.parent = new_node
        # We add the new node to the dict
        self.nodes[self.n] = new_node
        # If the tree was the root, the new node become the root
        if self.root.key == tree.key:
            self.root = self.nodes[self.n]

    def learn_one(self, x):
        x = utils.dict2numpy(x)
        # We create the node for x and add it to the tree
        if len(self.x_clusters.keys()) >= self.window_size:
            # Delete the oldest data point and add a node with the same key as the one deleted
            oldest_key = self.x_clusters[list(self.x_clusters.keys())[0]]
            oldest = self.nodes[oldest_key]
            if oldest.parent.left.key == oldest_key:
                oldest.parent.left = None
            else:
                oldest.parent.right = None
            del self.nodes[oldest_key]
            del self.x_clusters[list(self.x_clusters.keys())[0]]
            self.x_clusters[np.array2string(x)] = oldest_key
            self.nodes[oldest_key] = BinaryTreeNode(oldest_key, x)
        else:
            # Else we just add a node
            self.n += 1
            self.x_clusters[np.array2string(x)] = self.n
            self.nodes[self.n] = BinaryTreeNode(self.n, x)
        # We add it to the tree
        self.otd_clustering(self.root, x)
        return self

    def predict_otd(self, x, node, clusters):
        # get the list of predicted clusters for x
        if node is None:
            # If there is still no node in the tree
            return [1], -1
        if node.data is not None:
            # Add itself (n+1) and the key of the node that would merge x and node (n+2)
            clusters.extend([self.n + 2, self.n + 1])
            return clusters, node.key
        if self.intra_subtree_similarity(node) < self.inter_subtree_similarity(
            node, BinaryTreeNode(self.n + 1, x)
        ):
            # Add itself (n+1) and the key of the node that would merge x and node (n+2)
            clusters.extend([self.n + 2, self.n + 1])
            return clusters, node.key
        else:
            # Else, x wouls be added in the tree, we add the key of node
            clusters.extend([node.key])
            if self.inter_subtree_similarity(
                node.left, BinaryTreeNode(self.n + 1, x)
            ) > self.inter_subtree_similarity(node.right, BinaryTreeNode(self.n + 1, x)):
                # If  the right part of the tree is closer to x than the left part, we continue in the right part
                return self.predict_otd(x, node.right, clusters)
            else:
                # If  the left part of the tree is closer to x than the right part, we continue in the left part
                return self.predict_otd(x, node.left, clusters)

    def predict_one(self, x):
        """Predicts the clusters for a set of features `x`.

        Parameters
        ----------
        x
            A dictionary of features.
        Returns
        -------
        (list, int)
            A list of clusters (from node `x` to root) and the node to which it would have been merged.

        """
        x = utils.dict2numpy(x)
        # We predict to which cluster x would be if we added in the tree
        r, merged = self.predict_otd(x, self.root, [])
        r.reverse()
        return r, merged

    def find_path(self, root, path, k):
        # find the path from root to k
        # Adapted from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

        if root is None:
            # No path
            return False

        path.append(root)

        if root.key == k:
            return True

        if (root.left is not None and self.find_path(root.left, path, k)) or (
            root.right is not None and self.find_path(root.right, path, k)
        ):
            return True

        path.pop()
        return False

    def lca(self, i, j):
        # Find the least common ancestor
        # Adapted from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

        if self.root is None:
            return -1

        path_i = []
        path_j = []

        if not self.find_path(self.root, path_i, i) or not self.find_path(self.root, path_j, j):
            return -1

        k = 0
        while k < len(path_i) and k < len(path_j):
            if path_i[k] != path_j[k]:
                break
            k += 1
        return path_i[k - 1]

    def leaves(self, v):
        # find all the leaves from node v
        if v is None:
            # No leaves
            return -1
        if v.data is not None:
            # If v is a leaf, returns itself
            return [v]
        # Else, returns leaves from its children
        leave_list = []
        leave_list.extend(self.leaves(v.left))
        leave_list.extend(self.leaves(v.right))
        return leave_list

    def inter_subtree_similarity(self, tree_a, tree_b):
        # compute the mean distance (mean of distances) between two trees
        leaves_a = self.leaves(tree_a)
        leaves_b = self.leaves(tree_b)
        r = 0
        nb = 0
        for i, w_i in enumerate(leaves_a):
            for j, w_j in enumerate(leaves_b):
                nb += 1
                r += self.distance(w_i, w_j)
        return r / nb

    def intra_subtree_similarity(self, tree):
        # compute mean of distances between the nodes from a certain tree
        leaves = self.leaves(tree)
        r = 0
        nb = 0
        if len(leaves) == 1:
            return 0
        for i, w_i in enumerate(leaves):
            for j, w_j in enumerate(leaves):
                if i < j:
                    nb += 1
                    r += self.distance(w_i, w_j)
        return r / nb

    def __str__(self):
        self.print_tree(self.root)
        return "Printed Hierarchical Clustering Tree."

    def print_tree(self, node, level=0):
        # Print node and its children
        # Adapted from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(" " * 4 * level + "-> " + str(node.key))
            self.print_tree(node.left, level + 1)

    def get_parents(self, node):
        # Get all the parents of the node (the clusters it belongs to)
        clusters = [node.key]
        if node.parent is None:
            return clusters
        clusters.extend(self.get_parents(node.parent))
        return clusters

    def get_clusters_by_point(self):
        """Returns the list of clusters (from the data point node to the root) for all of the data points.

        Returns
        -------
        {x : list}
            A dict of all the data points with their clusters.
        """
        # Get all the clusters each data point belong to
        clusters = {}
        for x in self.x_clusters.keys():
            clusters[x] = self.get_parents(self.nodes[self.x_clusters[x]])
        return clusters

    def get_all_clusters(self):
        """Returns all the clusters of the tree.

        Returns
        -------
        {int : list}
            A dict of all the clusters with their children (or the data point for the leaves).
        """
        # Get the data of each cluster
        clusters = {}
        for i in range(1, self.n + 1):
            if self.nodes[i].data is not None:
                clusters[i] = [self.nodes[i].data]
            else:
                clusters[i] = [self.nodes[i].left.key, self.nodes[i].right.key]
        return sorted(clusters.items(), key=lambda x: len(x[1]))
