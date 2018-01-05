# TIMEOUT on some cases. Python too slow.
class DisjointSetForest:
    """Disjoint set forest with union by rank."""
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
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1


class DisjointSetNode:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0
        self.size = 1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Initialize graph.
n, m = map(int, input().strip().split())

edges = []
for edge in range(m):
    u, v, a, b = map(int, input().strip().split())
    if u != v:
        # Skip self-loops which cannot be in a tree.
        edges.append((u, v, a, b))


# Binary search on possible value for the maximum spanning tree fraction.
# sum(a_i)/sum(b_i) >= C => sum(a_i - C * b_i) >= 0
low = 0
high = 100
epsilon = 0.001
max_iterations = 60
iteration = 0
best_numerator = 1
best_denominator = 1

while high - low > epsilon and iteration < max_iterations:
    C = (low + high) / 2
    sum_a = 0
    sum_b = 0
    # Run Kruskal to find maximum spanning tree with weights a_i - C * b_i.
    disjoint_set_forest = DisjointSetForest()
    for vertex in range(n):
        disjoint_set_forest.make_set(vertex)
    # Sort edges by weight a_i - C * b_i in decreasing order.
    edges.sort(key=lambda x: x[2] - C * x[3], reverse=True)
    for edge in edges:
        u, v, a, b = edge
        if disjoint_set_forest.find_set(u) != disjoint_set_forest.find_set(v):
            disjoint_set_forest.union(u, v)
            sum_a += a
            sum_b += b
    # Now check whether it was possible to find a spanning tree with
    # corresponding value >= C.
    if sum_a - C * sum_b >= 0:
        low = C
        best_numerator = sum_a
        best_denominator = sum_b
    else:
        high = C
    iteration += 1

c = gcd(best_numerator, best_denominator)
print("{}/{}".format(best_numerator // c, best_denominator // c))

# Brute force optimization not good enough.
# class DisjointSetForest:
#     """Disjoint set forest with union by rank."""
#     def __init__(self):
#         self.node_map = {}

#     def make_set(self, key):
#         self.node_map[key] = DisjointSetNode(key)

#     def find_set(self, key):
#         return self._find_set(self.node_map[key])

#     def _find_set(self, x):
#         if x.parent is not x:
#             x.parent = self._find_set(x.parent)
#         return x.parent

#     def union(self, key1, key2):
#         self._union(self.find_set(key1), self.find_set(key2))

#     def _union(self, x, y):
#         if x is y:
#             return
#         if x.rank > y.rank:
#             y.parent = x
#         else:
#             x.parent = y
#             if x.rank == y.rank:
#                 y.rank += 1


# class DisjointSetNode:
#     def __init__(self, key):
#         self.key = key
#         self.parent = self
#         self.rank = 0
#         self.size = 1


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# # Initialize graph.
# n, m = map(int, input().strip().split())

# edges = []
# for edge in range(m):
#     u, v, a, b = map(int, input().strip().split())
#     if u != v:
#         # Skip self-loops which cannot be in a tree.
#         edges.append((u, v, a, b))

# disjoint_set_forest = DisjointSetForest()
# for vertex in range(n):
#     disjoint_set_forest.make_set(vertex)

# # Sort edges by ratio of a_i / b_i.
# edges.sort(key=lambda x: x[2] / x[3], reverse=True)
# # print(edges)

# # Run Kruskal to get an initial spanning tree.
# numerator = 0
# denominator = 0
# spanning_tree_edges = []
# for edge in edges:
#     u, v, a, b = edge
#     if disjoint_set_forest.find_set(u) != disjoint_set_forest.find_set(v):
#         disjoint_set_forest.union(u, v)
#         spanning_tree_edges.append(edge)
#         numerator += a
#         denominator += b

# # Now greedily swap edges improving ratio.
# modified = True
# while modified:
#     modified = False
#     new_spanning_tree_edges = list(spanning_tree_edges)
#     for edge in spanning_tree_edges:
#         (u, v, a, b) = edge

#         # Create new graph representing spanning tree minus current edge.
#         new_spanning_tree_edges.remove(edge)
#         new_disjoint_set_forest = DisjointSetForest()
#         for vertex in range(n):
#             new_disjoint_set_forest.make_set(vertex)
#         for e in new_spanning_tree_edges:
#             new_disjoint_set_forest.union(e[0], e[1])

#         # Find the single edge creating the best improvement.
#         best_edge = None
#         best_numerator = numerator
#         best_denominator = denominator
#         for candidate_edge in edges:
#             (u2, v2, a2, b2) = candidate_edge
#             if new_disjoint_set_forest.find_set(u2) != new_disjoint_set_forest.find_set(v2):
#                 if (numerator - a + a2) / (denominator - b + b2) > best_numerator / best_denominator:
#                     best_edge = candidate_edge
#                     best_numerator = numerator - a + a2
#                     best_denominator = denominator - b + b2
#         if best_edge is None:
#             # Replace original edge.
#             new_spanning_tree_edges.append(edge)
#         else:
#             modified = True
#             new_spanning_tree_edges.append(best_edge)
#             numerator, denominator = best_numerator, best_denominator
#     spanning_tree_edges = new_spanning_tree_edges

# c = gcd(numerator, denominator)
# print("{}/{}".format(numerator // c, denominator // c))
