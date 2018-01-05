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


# Merging Communities
N, Q = map(int, input().split())
disjoint_set_forest = DisjointSetForest()
for i in range(1, N + 1):
    disjoint_set_forest.make_set(i)
for query in range(Q):
    query = input().split()
    if query[0] == "M":
        i, j = int(query[1]), int(query[2])
        disjoint_set_forest.union(i, j)
    elif query[0] == "Q":
        i = int(query[1])
        print(disjoint_set_forest.find_set(i).size)
