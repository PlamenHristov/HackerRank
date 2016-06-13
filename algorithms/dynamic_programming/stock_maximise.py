def maximise_profit(prices):
    profit = 0
    max_price = 0
    for i in range(len(prices) - 1, -1, -1):  # reverse loop
        max_price = max(max_price, prices[i])
        profit += max_price - prices[i]
    print(profit)


num_tests = int(input())
for i in range(num_tests):
    n = input()
    num_input = input()
    prices = list(map(int, num_input.split(' ')))
    maximise_profit(prices)
