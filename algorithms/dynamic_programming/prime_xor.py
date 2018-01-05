# Passes all except one timeout with Pypy 3.
from collections import Counter


def solve(A, primes, mod):
    counter = Counter(A)
    unique_numbers = list(counter)
    m = len(counter)
    # dp[i][j] will be the number of multisets formed using
    # the first i unique numbers in A to xor to j.
    # a_i is at most 4500 so the xor will be less than 8192
    # (less than the next power of 2 larger).
    dp = [[0 for j in range(8192)] for i in range(m + 1)]
    # Initialize first row. There is one way to choose the empty set.
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(8192):
            x = unique_numbers[i - 1]
            y = j ^ x
            occurrences = counter[x]
            # We either include an even or odd number of occurrences of x.
            # An odd number will xor to x and an even number xor to 0.
            # Even case.
            dp[i][j] = dp[i - 1][j] * (1 + occurrences // 2)
            if y < 8192:
                # Odd case.
                dp[i][j] += dp[i - 1][y] * ((occurrences + 1) // 2)
            dp[i][j] %= mod

    total = 0
    for prime in primes:
        total = (total + dp[m][prime]) % mod
    return total


MOD = 1000000007

primes = []
is_prime = [True] * 8192
is_prime[0] = is_prime[1] = False
for x in range(2, 8192):
    if is_prime[x]:
        primes.append(x)
    for y in range(x, 8192, x):
        is_prime[y] = False

q = int(input())
for query in range(q):
    n = int(input())
    A = [int(s) for s in input().strip().split()]
    print(solve(A, primes, MOD))
