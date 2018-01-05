def check_pattern(A, B, i, j):
    """Checks whether the grid A has B as a sub-grid starting at position
    (i, j) of A as the top left corner of B"""
    R, C = len(A), len(A[0])
    r, c = len(B), len(B[0])
    if i + r > R or j + c > C:
        return False
    for m, row in enumerate(B):
        if A[i + m][j:j+c] != row:
            return False
    return True


T = int(input())
for test in range(T):
    R, C = map(int, input().split())
    A = []
    for row in range(R):
        A.append(input().strip())
    # print(A)
    r, c = map(int, input().split())
    B = []
    for row in range(r):
        B.append(input().strip())
    # print(B)
    possible = False
    for i, j in ((i, j) for i in range(R) for j in range(C)):
        if check_pattern(A, B, i, j):
            possible = True
            break
    print("YES" if possible else "NO")
