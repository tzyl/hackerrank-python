q = int(input())
for query in range(q):
    s = input().strip()
    pattern_count = 0
    i = 0
    while i < len(s):
        j = i + 1
        if s[i] == "1":
            while j < len(s) and s[j] == "0":
                j += 1
            if j < len(s) and j - i > 1 and s[j] == "1":
                pattern_count += 1
        i = j
    print(pattern_count)


# Using regular expressions.
import re


pattern = re.compile("10+(?=1)")
q = int(input())
for query in range(q):
    s = input().strip()
    print(len(re.findall(pattern, s)))
