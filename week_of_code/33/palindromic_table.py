n, m = map(int, input().split())
table = []
for row in range(n):
    table.append([int(s) for s in input().split()])

# def is_beautiful_rectangle(table, i, j, height, width):
#     """Returns True if the rectangle with top left corner at (i, j) and given
#     height and width can form a palindromic sequence with no leading zero.
#     """
#     if height == 1 and width == 1:
#         return True
#     non_zeros = 0
#     digits = [0] * 10
#     for x in range(i, i + height):
#         for y in range(j, j + width):
#             digit = table[x][y]
#             digits[digit] = (digits[digit] + 1) % 2
#             if digit != 0:
#                 non_zeros += 1
#     return sum(digits) <= 1 and non_zeros >= 2


x1, y1, x2, y2 = None, None, None, None
best_area = 0

# Brute force
# for i in range(n):
#     for j in range(m):
#         for height in range(1, n - i + 1):
#             for width in range(1, m - j + 1):
#                 if is_beautiful_rectangle(table, i, j, height, width):
#                     if height * width > best_area:
#                         best_area = height * width
#                         x1, y1 = i, j
#                         x2, y2 = i + height - 1, j + width - 1

# print(best_area)
# print(x1, y1, x2, y2)

# DP
# def count_digits(table, i, j, height, width):
#     if (i, j, height, width - 1) in digits_cache:
#         digits = digits_cache[(i, j, height, width - 1)]
#         digits ^= digits_cache[(i, j + width - 1, height, 1)]
#     else:
#         digits = 0
#         for x in range(i, i + height):
#             for y in range(j, j + width):
#                 digits ^= 1 << table[x][y]
#     digits_cache[(i, j, height, width)] = digits
#     return digits


# def count_digits(table, i, j, height, width):
#     if (i, j, height - 1, width) in digits_cache:
#         digits = list(digits_cache[(i, j, height - 1, width)])
#         x = i + height - 1
#         for y in range(j, j + width):
#             digits[table[x][y]] += 1
#     elif (i, j, height, width - 1) in digits_cache:
#         digits = list(digits_cache[(i, j, height, width - 1)])
#         y = j + width - 1
#         for x in range(i, i + height):
#             digits[table[x][y]] += 1
#     else:
#         digits = [0] * 10
#         for x in range(i, i + height):
#             for y in range(j, j + width):
#                 digits[table[x][y]] += 1
#     digits_cache[(i, j, height, width)] = digits
#     return digits


# digits_cache = {}


def is_beautiful_rectangle(i, j, height, width):
    if height == 1 and width == 1:
        return True
    digit_count = calculate_rectangle_digit_count(i, j, height, width)
    return sum(x % 2 for x in digit_count) <= 1 and sum(digit_count[1:]) >= 2


def calculate_rectangle_digit_count(i, j, height, width):
    A = rectangle_cache[i][j]
    if i + height < n and j + width < m:
        B = rectangle_cache[i + height][j]
        C = rectangle_cache[i][j + width]
        D = rectangle_cache[i + height][j + width]
    elif i + height < n:
        B = rectangle_cache[i + height][j]
        C = tuple(0 for digit in range(10))
        D = tuple(0 for digit in range(10))
    elif j + width < m:
        B = tuple(0 for digit in range(10))
        C = rectangle_cache[i][j + width]
        D = tuple(0 for digit in range(10))
    else:
        B = tuple(0 for digit in range(10))
        C = tuple(0 for digit in range(10))
        D = tuple(0 for digit in range(10))

    digit_count = tuple(A[i] - B[i] - C[i] + D[i] for i in range(10))
    return digit_count


# rectangle_cache[i][j] will contain a list of digit counts for the rectangle
# with top left corner (i, j) and bottom right corner (n - 1, m - 1).
rectangle_cache = [[None for column in range(m)] for row in range(n)]

for height in range(1, n + 1):
    digit_count = [0] * 10
    for width in range(1, m + 1):
        i = n - height
        j = m - width
        for x in range(i, n):
            digit_count[table[x][j]] += 1
        rectangle_cache[i][j] = tuple(digit_count)

for height in range(1, n + 1):
    for width in range(1, m + 1):
        if height * width <= best_area:
            continue
        for i in range(n - height + 1):
            if height * width <= best_area:
                break
            for j in range(m - width + 1):
                if is_beautiful_rectangle(i, j, height, width):
                    if height * width > best_area:
                        best_area = height * width
                        x1, y1 = i, j
                        x2, y2 = i + height - 1, j + width - 1
                        break

print(best_area)
print(x1, y1, x2, y2)
