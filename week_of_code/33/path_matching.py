# NOT WORKING
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


class Tree:
    def __init__(self):
        self.root = None


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.parent = None
        self.letter = None
        self.count = 0
        self.reverse_count = 0


class AdjacencyList:
    """Adjacency list for a graph with vertices 1,...,n."""
    def __init__(self, n):
        self.adj = [[] for vertex in range(n)]

    def add_edge(self, u, v):
        self.adj[u - 1].append(v)
        self.adj[v - 1].append(u)

    def add_directed_edge(self, u, v):
        self.adj[u - 1].append(v)

    def get_neighbours(self, v):
        return self.adj[v - 1]


import re
import sys
sys.setrecursionlimit(100000)

n, q = map(int, input().split())
s = input().strip()
p = input().strip()

# Create graph.
adjacency_list = AdjacencyList(n)
for edge in range(n - 1):
    u_key, v_key = map(int, input().split())
    adjacency_list.add_edge(u_key, v_key)

# Convert to rooted tree.
tree_node_map = {}
for vertex_key in range(1, n + 1):
    tree_node_map[vertex_key] = TreeNode(vertex_key)
    tree_node_map[vertex_key].letter = s[vertex_key - 1]
# Initialize 1 as the root of the tree.
root = tree_node_map[1]
root.parent = root
# DFS to build tree starting from 1 as the root.
# previous word lengths to keep track of how deep we are in the DFS.
current_word = []
stack = [1]
previous_word_lengths = [0]
seen = set([1])

while stack:
    u_key = stack.pop()
    u = tree_node_map[u_key]
    previous_word_length = previous_word_lengths.pop()
    # Update current word for this path.
    while len(current_word) > previous_word_length:
        current_word.pop()
    current_word.append(u.letter)
    # Calculate counts of p in current word.
    u.count = u.parent.count
    u.reverse_count = u.parent.reverse_count
    suffix = "".join(current_word[-len(p):])
    if p == suffix:
        u.count += 1
    if p == suffix[::-1]:
        u.reverse_count += 1
    # Check neighbours.
    for v_key in adjacency_list.get_neighbours(u_key):
        if v_key not in seen:
            seen.add(v_key)
            stack.append(v_key)
            previous_word_lengths.append(len(current_word))
            v = tree_node_map[v_key]
            u.children.append(v)
            v.parent = u

# TEST: traverse rooted tree
# from collections import deque
# queue = deque([root])
# print(s)
# print(p)
# while queue:
#     u = queue.popleft()
#     print(u.key, u.parent.key, u.letter, u.count, u.reverse_count)
#     for v in u.children:
#         queue.append(v)


# Tarjan's offline lowest common ancestor.
def tarjan_olca(u_key):
    disjoint_set_forest.make_set(u_key)
    ancestors[u_key] = u_key
    u = tree_node_map[u_key]
    for v in u.children:
        v_key = v.key
        tarjan_olca(v_key)
        disjoint_set_forest.union(u_key, v_key)
        ancestors[disjoint_set_forest.find_set(u_key).key] = u_key
    finished.add(u_key)
    for v_key in query_adjacency_list.get_neighbours(u_key):
        if v_key in finished:
            lca_key = ancestors[disjoint_set_forest.find_set(v_key).key]
            answers[(u_key, v_key)] = calculate_query(u_key, v_key, lca_key)
            answers[(v_key, u_key)] = calculate_query(v_key, u_key, lca_key)


def calculate_query(u_key, v_key, lca_key):
    """Calculates the answer for a query given their lowest common ancestor."""
    u = tree_node_map[u_key]
    v = tree_node_map[v_key]
    lca = tree_node_map[lca_key]

    # u_count = u.reverse_count - lca.reverse_count
    # v_count = v.count - lca.count
    # Intersection counts

    # Brute force O(h) here.
    # Ideally want to just have to calculate intersections for O(p).
    u_word = []
    x = u
    while x is not lca:
        u_word.append(x.letter)
        x = x.parent

    v_word = []
    y = v
    while y is not lca:
        v_word.append(y.letter)
        y = y.parent

    s_prime = "".join(u_word + [lca.letter] + v_word[::-1])

    return sum(1 for _ in re.finditer("(?=" + p + ")", s_prime))


queries = []
answers = {}
query_adjacency_list = AdjacencyList(n)
for query in range(q):
    u_key, v_key = map(int, input().split())
    query_adjacency_list.add_edge(u_key, v_key)
    queries.append((u_key, v_key))

disjoint_set_forest = DisjointSetForest()
ancestors = {}
finished = set()
# Run Tarjan's OLCA from root 1.
tarjan_olca(1)

# Print out answers to queries in order.
for u_key, v_key in queries:
    print(answers[(u_key, v_key)])
