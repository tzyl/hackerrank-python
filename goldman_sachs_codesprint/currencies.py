from math import log


# O(n^3*log(m))
def currencies(n, x, s, f, m, A):
    mod = 1000000007
    log_A = [[log(A[i][j]) if A[i][j] else -float("inf") for j in range(n)] for i in range(n)]
    matrix, log_matrix = calculate_transformation_matrix(m, A, log_A)
    return x * matrix[s][f] % mod


def calculate_transformation_matrix(m, A, log_A):
    if m == 1:
        return A, log_A
    elif m % 2 == 0:
        sqrt_matrix, sqrt_log_matrix = calculate_transformation_matrix(m // 2, A, log_A)
        return combine_transformation_matrix(sqrt_matrix, sqrt_matrix, sqrt_log_matrix, sqrt_log_matrix)
    else:
        prev_matrix, prev_log_matrix = calculate_transformation_matrix(m - 1, A, log_A)
        return combine_transformation_matrix(prev_matrix, A, prev_log_matrix, log_A)


# O(n^3)
def combine_transformation_matrix(A, B, log_A, log_B):
    mod = 1000000007
    n = len(A)
    C = [[None for j in range(n)] for i in range(n)]
    log_C = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            best_log = -float("inf")
            best = 0
            for k in range(n):
                if log_A[i][k] + log_B[k][j] > best_log:
                    best_log = log_A[i][k] + log_B[k][j]
                    best = A[i][k] * B[k][j] % mod
            log_C[i][j] = best_log
            C[i][j] = best
    return C, log_C


if __name__ == "__main__":
    n = int(input().strip())
    x, s, f, m = input().strip().split(' ')
    x, s, f, m = [int(x), int(s), int(f), int(m)]
    A = []
    for i in range(n):
        row = [int(s) for s in input().strip().split(' ')]
        A.append(row)
    print(currencies(n, x, s, f, m, A))
