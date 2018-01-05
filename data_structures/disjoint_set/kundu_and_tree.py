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


# Kundu and Tree
def triplets(n):
    """Calculates n choose 3"""
    return (n * (n - 1) * (n - 2) // 6)


def pairs(n):
    """Calculates n choose 2"""
    return (n * (n - 1) // 2)


N = int(input())
disjoint_set_forest = DisjointSetForest()
for vertex in range(1, N + 1):
    disjoint_set_forest.make_set(vertex)
# Create components connected by bad edges.
for edge_index in range(N - 1):
    edge = input().split()
    colour = edge[-1]
    if colour == "b":
        disjoint_set_forest.union(int(edge[0]), int(edge[1]))
# Find the bad components.
bad_component_keys = set()
for vertex in range(1, N + 1):
    component = disjoint_set_forest.find_set(vertex)
    if component.key not in bad_component_keys:
        bad_component_keys.add(component.key)
# Calculate how many bad triplets there are from the bad comoponents.
# A bad triplet would use either two or three vertices in the same
# bad component.
bad_triplets = 0
for bad_component_key in bad_component_keys:
    bad_component = disjoint_set_forest.find_set(bad_component_key)
    bad_triplets += triplets(bad_component.size)
    bad_triplets += pairs(bad_component.size) * (N - bad_component.size)
    bad_triplets %= 10 ** 9 + 7
good_triplets = (triplets(N) - bad_triplets) % (10 ** 9 + 7)
print(good_triplets)
