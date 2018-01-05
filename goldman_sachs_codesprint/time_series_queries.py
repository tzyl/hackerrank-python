def find_next_value(values, v):
    """Finds next value greater than or equal to v in sorted list values
    or returns None if no such exists.
    """
    if v > values[-1]:
        return None
    p = 0
    r = len(values)
    while p < r:
        q = (p + r) // 2
        if v > values[q]:
            p = q + 1
        else:
            r = q
    return values[p]


if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    t = list(map(int, input().strip().split(' ')))
    p = list(map(int, input().strip().split(' ')))
    # Process to find time of first ocurrence of each price
    # and max price after each time point.
    max_price_after = {}
    current_max_price = 0
    for time, price in zip(reversed(t), reversed(p)):
        current_max_price = max(current_max_price, price)
        max_price_after[time] = current_max_price
    first_occurrence = {}
    for time, price in zip(t, p):
        if price not in first_occurrence:
            first_occurrence[price] = time
    first_time_greater_than = {}
    earliest_time = float("inf")
    sorted_p = sorted(set(p))
    for price in reversed(sorted_p):
        earliest_time = min(earliest_time, first_occurrence[price])
        first_time_greater_than[price] = earliest_time
    # Answer queries using processed information.
    for a0 in range(q):
        _type, v = input().strip().split(' ')
        _type, v = [int(_type), int(v)]
        if _type == 1:
            key = find_next_value(sorted_p, v)
            result = first_time_greater_than[key] if key is not None else -1
        elif _type == 2:
            key = find_next_value(t, v)
            result = max_price_after[key] if key is not None else -1
        print(result)
