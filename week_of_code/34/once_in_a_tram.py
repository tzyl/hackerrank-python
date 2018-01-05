def is_lucky(x):
    if x < 10**5 or x >= 10**6:
        return False
    left_sum = right_sum = 0
    for digit in range(3):
        right_sum += x % 10
        x //= 10
    for digit in range(3):
        left_sum += x % 10
        x //= 10
    return left_sum == right_sum


x = int(input().strip())
x += 1
while not is_lucky(x):
    x += 1
print(x)
