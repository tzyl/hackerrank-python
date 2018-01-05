# O(n) using hashmap
def solve(m, n, c):
    seen_at = {}
    for index, cost in enumerate(c):
        target = m - cost
        if target in seen_at:
            return (seen_at[target] + 1, index + 1)
        seen_at[cost] = index
    return None


# O(nlogn) for sorting
def solve2(m, n, c):
    sorted_c = sorted(c)
    i = 0
    j = n - 1
    while sorted_c[i] + sorted_c[j] != m:
        if sorted_c[i] + sorted_c[j] > m:
            j -= 1
        if sorted_c[i] + sorted_c[j] < m:
            i += 1
    for index, cost in enumerate(c):
        if cost == sorted_c[i]:
            index1 = index
            break
    for index, cost in enumerate(c):
        if cost == sorted_c[j] and index != index1:
            index2 = index
            break
    return (min(index1, index2) + 1, max(index1, index2) + 1)


t = int(input())
for case in range(t):
    m = int(input())
    n = int(input())
    c = [int(s) for s in input().strip().split()]
    print(*solve(m, n, c))
