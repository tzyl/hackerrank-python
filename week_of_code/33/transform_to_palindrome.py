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


def longest_palindrome_subsequence(s):
    """USING DP O(n^2)"""
    A = [[1] * len(s) for _ in range(len(s))]
    for length in range(2, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if j == i + 1:
                    A[i][j] = 2
                else:
                    A[i][j] = A[i + 1][j - 1] + 2
            elif s[i] != s[j]:
                if A[i + 1][j] > A[i][j - 1]:
                    A[i][j] = A[i + 1][j]
                else:
                    A[i][j] = A[i][j - 1]
    return A[0][len(s) - 1]


n, k, m = map(int, input().split())

# Group letters into equivalence classes under the binary relation.
equivalence_classes = DisjointSetForest()
for letter in range(1, n + 1):
    equivalence_classes.make_set(letter)
for transformation in range(k):
    i, j = map(int, input().split())
    equivalence_classes.union(i, j)

# Transform the string using the representatives of each equivalence class.
s = [int(c) for c in input().split()]
transformed_s = [equivalence_classes.find_set(x).key for x in s]

# Run LPS using DP O(n^2) on the transformed string.
print(longest_palindrome_subsequence(transformed_s))
