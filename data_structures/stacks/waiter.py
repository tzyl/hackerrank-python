def is_prime(x):
    if x <= 1:
        return False
    factor = 2
    while factor * factor <= x:
        if x % factor == 0:
            return False
        factor += 1
    return True


N, Q = map(int, input().split())
A = [int(s) for s in input().split()]
prime = 0
for iteration in range(1, Q + 1):
    # Increment until we find the next prime number.
    prime += 1
    while not is_prime(prime):
        prime += 1
    A_iteration = []
    B_iteration = []
    while A:
        x = A.pop()
        if x % prime == 0:
            B_iteration.append(x)
        else:
            A_iteration.append(x)
    # Print out elements of B_iteration
    while B_iteration:
        print(B_iteration.pop())
    A = A_iteration
# Print out leftover elements.
while A:
    print(A.pop())
