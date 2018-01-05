from collections import defaultdict


class DisjointSetForest:
    """Disjoint set forest with union by size."""
    def __init__(self):
        self.node_map = {}

    def make_set(self, key):
        self.node_map[key] = DisjointSetNode(key)

    def find_set(self, key):
        return self._find_set(self.node_map[key])

    def _find_set(self, x):
        if x.parent is not x:
            x.parent = self._find_set(x.parent)
        return x.parent

    def union(self, key1, key2):
        self._union(self.find_set(key1), self.find_set(key2))

    def _union(self, x, y):
        if x is y:
            return
        if x.size > y.size:
            y.parent = x
            y.parent.size += y.size
        else:
            x.parent = y
            x.parent.size += x.size


class DisjointSetNode:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0
        self.size = 1


def initialize_disjoint_set_forest(n):
    """Initializes disjoint set forest with vertices labelled 1 to n."""
    disjoint_set_forest = DisjointSetForest()
    for vertex in range(1, N + 1):
        disjoint_set_forest.make_set(vertex)
    return disjoint_set_forest


def binary_search_floor_weight(w, edges):
    """Finds the largest weight <= w present in edges using binary search."""
    if w < edges[0][-1]:
        return 0
    p, r = 0, len(edges) - 1
    while p < r:
        q = (p + r + 1) // 2
        if edges[q][-1] == w:
            return w
        elif edges[q][-1] > w:
            r = q - 1
        else:
            p = q
    return edges[p][-1]


# Super Maximum Cost Queries
N, Q = map(int, input().split())
disjoint_set_forest = initialize_disjoint_set_forest(N)
cumulative_count = {0: 0}
edges = []
for edge_index in range(N - 1):
    edge = tuple(map(int, input().split()))
    edges.append(edge)
edges.sort(key=lambda x: x[-1])
# Go through edges from smallest to largest and calculate cumulative number of
# paths with cost less than or equal to current edge weight.
total = 0
for edge in edges:
    weight = edge[-1]
    total += (disjoint_set_forest.find_set(edge[0]).size *
              disjoint_set_forest.find_set(edge[1]).size)
    disjoint_set_forest.union(edge[0], edge[1])
    cumulative_count[weight] = total
# Now answer each query with cumulative_count but need to find actual weights
# of edges in the tree rather than L, R.
for query in range(Q):
    L, R = map(int, input().split())
    lower_weight = binary_search_floor_weight(L - 1, edges)
    upper_weight = binary_search_floor_weight(R, edges)
    print(cumulative_count[upper_weight] - cumulative_count[lower_weight])
