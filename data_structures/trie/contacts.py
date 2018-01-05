# RUNTIME ERROR ON CASE #12. Think problem designed too slow for Python.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                current.links[c] = TrieNode()
            current = current.links[c]
            current.size += 1
        current.isWord = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                return False
            current = current.links[c]
        return current.isWord

    def starts_with_count(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.links:
                return 0
            current = current.links[c]
        return current.size

    def starts_with(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.links:
                return False
            current = current.links[c]
        return True


class TrieNode:
    def __init__(self):
        self.links = {}
        self.isWord = False
        self.size = 0


n = int(input())
trie = Trie()
for line in range(n):
    operation, s = input().split()
    if operation == "add":
        trie.insert(s)
    elif operation == "find":
        print(trie.starts_with_count(s))

# with open("output.txt") as f:
#     output = [l for l in (line.strip() for line in f) if l]


# with open("test.txt") as f:
#     answers = iter(output)
#     n = int(next(f))
#     print(n)
#     trie = Trie()
#     for line in f:
#         # print(line)
#         operation, s = line.split()
#         if operation == "add":
#             trie.insert(s)
#         elif operation == "find":
#             ans = trie.starts_with_count(s)
#             expected_ans = int(next(answers))
#             if ans != expected_ans:
#                 print(ans, expected_ans)
