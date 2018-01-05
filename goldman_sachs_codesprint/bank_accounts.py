def fee_or_upfront(n, k, x, d, p):
    fees = 0
    for price in p:
        fees += max(k, x * price / 100)
    return "fee" if fees <= d else "upfront"


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k, x, d = input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = list(map(int, input().strip().split(' ')))
        result = fee_or_upfront(n, k, x, d, p)
        print(result)
