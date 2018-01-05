n = int(input())
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]
i1 = min(range(n), key=lambda i: A[i])
i2 = min((i for i in range(n) if i != i1), key=lambda i: A[i])
j1 = min(range(n), key=lambda j: B[j])
j2 = min((j for j in range(n) if j != j1), key=lambda j: B[j])
# Check if the smallest elements in A and B are valid, otherwise pick the next
# best combination.
if i1 != j1:
    print(A[i1] + B[j1])
else:
    print(min(A[i1] + B[j2], A[i2] + B[j1]))
