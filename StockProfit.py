#stocks_prices = [10, 7, 5, 8, 11, 9, 10, 1, 8]
stocks_prices = [10, 8, 5, 4, 6, 3, 6, 8, 1, 7]

def get_max_profit(stocks):
    profit = stocks[-1] - stocks[0]
    stocks_sorted = sorted(stocks[:len(stocks_prices)-1])
    for i in stocks_sorted:
        new_profit = max(stocks[stocks.index(i)+1:])
        if new_profit - i > profit:
            profit = new_profit - i
        else:
            return profit
    return profit

def get_max_profit2(stocks):
    profit = []
    max_profit = stocks[-1]
    min = stocks[0]
    for i in range(1, len(stocks)):
        if stocks[i] < stocks[i - 1] and i < stocks.index(max_profit):
            min = stocks[i]
        elif stocks[i] > stocks[i - 1]:
            max_profit = stocks[i]
        elif i < stocks.index(max_profit):
            profit.append(max_profit - min)
            min = stocks[i]
            max_profit = stocks[-1]
    profit.append(max_profit - min)
    return max(profit)


print get_max_profit(stocks_prices)
