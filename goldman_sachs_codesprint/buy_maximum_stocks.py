def buy_maximum_stocks(n, k, A):
    # Calculate the number of stocks available at each price.
    price_to_available = {}
    for i, price in enumerate(A, 1):
        if price not in price_to_available:
            price_to_available[price] = 0
        price_to_available[price] += i
    # Greedily buy as many as possible at the cheapest price.
    current_funds = k
    number_of_stocks = 0
    for price in sorted(set(A)):
        number_available = price_to_available[price]
        number_possible = current_funds // price
        number_bought = min(number_available, number_possible)
        current_funds -= number_bought * price
        number_of_stocks += number_bought
    return number_of_stocks


if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buy_maximum_stocks(n, k, A)
    print(result)
