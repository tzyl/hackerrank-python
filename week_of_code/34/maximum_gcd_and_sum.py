# Python too slow. Java implementation works.
n = int(input())
A = [int(s) for s in input().strip().split()]
B = [int(s) for s in input().strip().split()]
A_check = B_check = 0
result = 0
for i in range(n):
    A_check |= 1 << A[i]
    B_check |= 1 << B[i]

for d in range(1, 1000000 + 1):
    A_possible = []
    B_possible = []
    for i in range(1, 1000000 // d + 1):
        x = i * d
        if A_check & 1 << x:
            A_possible.append(x)
        if B_check & 1 << x:
            B_possible.append(x)
    if A_possible and B_possible:
        # This divisor is the highest possible so far.
        # Get the best possible pair sum.
        result = A_possible[-1] + B_possible[-1]
print(result)
