# O(n^3 logn)
T = int(input())
for testcase in range(T):
    s = input().strip()
    equivalence_classes = {}
    for length in range(1, len(s)):
        for i in range(len(s) - length + 1):
            equivalence_class = "".join(sorted(s[i:i + length]))
            if equivalence_class not in equivalence_classes:
                equivalence_classes[equivalence_class] = 1
            else:
                equivalence_classes[equivalence_class] += 1
    print(sum(count * (count - 1) // 2 for
              count in equivalence_classes.values()))

# Brute force O(n^4) too slow.
# from collections import Counter


# def is_anagram(s1, s2):
#     return Counter(s1) == Counter(s2)


# T = int(input())
# for testcase in range(T):
#     s = input().strip()
#     anagram_count = 0
#     for length in range(1, len(s)):
#         for i in range(len(s) - length + 1):
#             for j in range(i + 1, len(s) - length + 1):
#                 if is_anagram(s[i:i + length], s[j: j + length]):
#                     anagram_count += 1
#     print(anagram_count)
