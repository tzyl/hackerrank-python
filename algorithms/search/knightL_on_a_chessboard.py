from collections import deque


def find_minimum_moves(a, b, n):
    # Breadth first search. Distance of -1 indicates not possible
    # for KnightL(a, b) to reach (i, j) from (0, 0).
    dx = [a, a, b, b, -a, -a, -b, -b]
    dy = [b, -b, a, -a, b, -b, a, -a]
    distance = [[-1 for i in range(n)] for i in range(n)]
    distance[0][0] = 0
    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        for x, y in zip(dx, dy):
            u = i + x
            v = j + y
            if 0 <= u < n and 0 <= v < n:
                if distance[u][v] == -1:
                    distance[u][v] = distance[i][j] + 1
                    queue.append((u, v))
    return distance[n - 1][n - 1]


n = int(input())
result = [[-1 for i in range(n - 1)] for i in range(n - 1)]
for a in range(1, n):
    for b in range(1, n):
        result[a - 1][b - 1] = find_minimum_moves(a, b, n)
print("\n".join(" ".join(str(d) for d in row) for row in result))
