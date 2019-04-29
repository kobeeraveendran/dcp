def max_profit(stock_prices):

    l = len(stock_prices)
    max_sale = 0

    for i in range(l - 1):
        max_val = max(stock_prices[i + 1:])

        curr_profit = max_val - stock_prices[i]

        if curr_profit > max_sale:
            max_sale = curr_profit

    return max_sale

test1 = [9, 11, 8, 5, 7, 10]

print(max_profit(test1))