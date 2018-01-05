def calculate_median(counts, d):
    """Calculates the median expenditure value of the past d days given
    the counts of the expenditure values between 0 and 200 inclusive.
    """
    cumulative_count = 0
    for expenditure, count in enumerate(counts):
        cumulative_count += count
        if cumulative_count > (d + 1) // 2:
            # This value is certainly the median.
            return expenditure
        elif cumulative_count == (d + 1) // 2:
            if d % 2 == 1:
                return expenditure
            else:
                next_expenditure = expenditure + 1
                while not counts[next_expenditure]:
                    next_expenditure += 1
                return (expenditure + next_expenditure) / 2


n, d = map(int, input().split())
counts = [0] * 201
expenditures = [int(s) for s in input().split()]

for i in range(d):
    counts[expenditures[i]] += 1

notification_count = 0
for i in range(d, n):
    if expenditures[i] >= 2 * calculate_median(counts, d):
        notification_count += 1
    counts[expenditures[i - d]] -= 1
    counts[expenditures[i]] += 1

print(notification_count)
