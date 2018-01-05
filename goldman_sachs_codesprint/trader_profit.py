def trader_profit(k, n, A):
    # P[i][j] gives the maximum profit with at most i transactions
    # up to the jth day (days are 0-indexed).
    P = [[0 for j in range(n)] for i in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n):
            # We either complete a transaction (sell) or don't on the jth day.
            best = P[i][j - 1]
            for m in range(j):
                best = max(best, A[j] - A[m] + P[i - 1][m])
            P[i][j] = best
    return P[k][n - 1]


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        k = int(input().strip())
        n = int(input().strip())
        A = list(map(int, input().strip().split(' ')))
        result = trader_profit(k, n, A)
        print(result)
