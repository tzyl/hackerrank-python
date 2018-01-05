n = int(input())
S = input().strip().split()

# Greedily pick the longest prefix in chain (lexicographically largest) then
# mark the smaller prefix neighbour as invalid.
S.sort(reverse=True)
prefix_set = set(S)
invalid = set()
benefit = 0
for prefix in S:
    if prefix not in invalid:
        benefit += sum(ord(c) for c in prefix)
        # Add the smaller prefix neighbour of prefix to invalid if it exists.
        for i in range(1, len(prefix)):
            if prefix[:-i] in prefix_set:
                invalid.add(prefix[:-i])
                break
print(benefit)


# Trie version of greedy solution. Too much memory?
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.node_map = {}

#     def insert(self, word):
#         current = self.root
#         for c in word:
#             if c not in current.links:
#                 current.links[c] = TrieNode()
#                 current.links[c].parent = current
#             current = current.links[c]
#         current.is_word = True
#         self.node_map[word] = current

#     def mark_prefix_neighbour_invalid(self, word):
#         """Marks the shorter prefix neighbour of word as invalid. If there
#         does not exist one then root is marked as invalid.
#         """
#         if word not in self.node_map:
#             return
#         current = self.node_map[word].parent
#         while current.parent is not None and not current.is_word:
#             current = current.parent
#         current.is_valid = False


# class TrieNode:
#     def __init__(self):
#         self.links = {}
#         self.parent = None
#         self.is_word = False
#         self.is_valid = True


# def calculate_benefit(prefix):
#     """Calculates the sum of the ASCII values of the characters in prefix."""
#     return sum(ord(c) for c in prefix)


# n = int(input())
# S = input().strip().split()

# trie = Trie()
# for prefix in S:
#     trie.insert(prefix)

# # Greedily pick the longest prefix in chain and mark its shorter
# # prefix neighbour as invalid.
# S.sort(key=lambda s: sum(ord(c) for c in s), reverse=True)
# benefit = 0
# for prefix in S:
#     if trie.node_map[prefix].is_valid:
#         benefit += calculate_benefit(prefix)
#         trie.mark_prefix_neighbour_invalid(prefix)
# print(benefit)
