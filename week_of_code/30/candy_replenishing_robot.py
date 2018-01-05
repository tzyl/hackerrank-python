n, t = input().strip().split(' ')
n, t = [int(n), int(t)]
c = [int(s) for s in input().strip().split()]
candies = n
added = 0
for i in range(t - 1):
    candies -= c[i]
    if candies < 5:
        added += n - candies
        candies = n
print(added)
