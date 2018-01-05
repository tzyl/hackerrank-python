N, M = map(int, input().split())
start = [0] * (N + 1)
end = [0] * (N + 1)
for operation in range(M):
    a, b, k = map(int, input().split())
    start[a] += k
    end[b] += k
current = 0
maximum = 0
for x, y in zip(start, end):
    current += x
    maximum = max(maximum, current)
    current -= y
print(maximum)
