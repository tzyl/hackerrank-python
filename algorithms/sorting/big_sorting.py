from functools import cmp_to_key


def compare_digit_strings(s1, s2):
    """Compares digit strings s1 and s2 as integers.
    Returns 1 if s1 > s2, -1 if s1 < s2 or 0 if s1 = s2.
    """
    if len(s1) > len(s2):
        return 1
    elif len(s2) > len(s1):
        return -1
    for c1, c2 in zip(s1, s2):
        if int(c1) > int(c2):
            return 1
        elif int(c1) < int(c2):
            return -1
    return 0


n = int(input())
A = [input() for i in range(n)]
A.sort(key=cmp_to_key(compare_digit_strings))
for x in A:
    print(x)
