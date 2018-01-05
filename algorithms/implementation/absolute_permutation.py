T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    if K == 0:
        print(" ".join(str(x) for x in range(1, N + 1)))
    elif N % (2 * K) != 0:
        print(-1)
    else:
        A = list(range(1, N + 1))
        for block in range(N // (2 * K)):
            for i in range(K):
                A[(block * 2 * K) + i], A[(block * 2 * K) + i + K] = A[(block * 2 * K) + i + K], A[(block * 2 * K) + i]
        print(" ".join(str(x) for x in A))
