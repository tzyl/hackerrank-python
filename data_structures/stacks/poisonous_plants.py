N = int(input())
A = [int(s) for s in input().split()]
stack = []
days_till_deaths = []
max_days_till_death = 0
for x in A:
    # block is the maximum number of days till the death of consecutive
    # not smaller plants to the left.
    block = 0
    while stack and stack[-1] >= x:
        stack.pop()
        block = max(block, days_till_deaths.pop())
    if stack:
        # This plant definitely dies after block + 1 days.
        stack.append(x)
        days_till_deaths.append(block + 1)
        max_days_till_death = max(max_days_till_death, block + 1)
    else:
        # This plant will always survive.
        stack.append(x)
        days_till_deaths.append(0)
print(max_days_till_death)
