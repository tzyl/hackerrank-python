n, k = map(int, input().strip().split())
A = [int(s) for s in input().strip().split()]
A.sort()
# left is index of left most house covered by transmitter at index middle.
left = middle = 0
transmitters = 0
while left < n:
    transmitters += 1
    # Place transmitter in the furthest position which still covers left.
    while middle < n - 1 and A[middle + 1] <= A[left] + k:
        middle += 1
    # Find furthest right house still covered by transmitter.
    right = middle
    while right < n - 1 and A[right + 1] <= A[middle] + k:
        right += 1
    left = middle = right + 1
print(transmitters)
