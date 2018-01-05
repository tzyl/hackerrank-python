# Could use DFS rather than union find as graph is static.
class DisjointSetForestSize:
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


N, P = map(int, input().split())
# Create set representatives for each astronaut.
disjoint_set_forest = DisjointSetForestSize()
for astronaut in range(N):
    disjoint_set_forest.make_set(astronaut)
# Pair up astronauts from the same country.
for pair in range(P):
    i, j = map(int, input().split())
    disjoint_set_forest.union(i, j)
# Pick out the representatives of the individual countries.
countries = []
seen = set()
for astronaut in range(N):
    country = disjoint_set_forest.find_set(astronaut)
    if country.key not in seen:
        seen.add(country.key)
        countries.append(country)
# Calculate the number of ways of picking a pair of astronauts
# from different countries.
number_of_ways = N * (N - 1) // 2
for country in countries:
    number_of_ways -= country.size * (country.size - 1) // 2
print(number_of_ways)
