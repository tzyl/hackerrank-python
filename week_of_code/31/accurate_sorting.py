def is_sortable(A):
    """Returns True if A is sortable by only swapping elements which differ
    by one or False otherwise.
    """
    for i, x in enumerate(A):
        if abs(i - x) > 1:
            return False
    return True


q = int(input())
for query in range(q):
    n = int(input())
    A = [int(s) for s in input().split()]
    print("Yes" if is_sortable(A) else "No")
