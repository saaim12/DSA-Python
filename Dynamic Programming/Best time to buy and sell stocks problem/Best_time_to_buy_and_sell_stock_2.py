def best_time_to_buy_and_sell_stock_2(arr):
    n = len(arr)

    def check(idx, can_buy):
        if idx == n:
            return 0

        if can_buy:
            # Option 1: Buy now (-arr[idx]) and go to sell
            # Option 2: Skip buying
            return max(-arr[idx] + check(idx + 1, False), check(idx + 1, True))
        else:
            # Option 1: Sell now (+arr[idx]) and go to buy
            # Option 2: Skip selling
            return max(arr[idx] + check(idx + 1, True), check(idx + 1, False))

    return check(0, True)

# Example test
prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_and_sell_stock_2(prices))  # Output: 7

def best_time_to_buy_and_sell_stock_2_memo(arr):
    n = len(arr)
    memo = {}

    def check(idx, can_buy):
        if idx == n:
            return 0
        if (idx, can_buy) in memo:
            return memo[(idx, can_buy)]

        if can_buy:
            profit = max(-arr[idx] + check(idx + 1, False), check(idx + 1, True))
        else:
            profit = max(arr[idx] + check(idx + 1, True), check(idx + 1, False))

        memo[(idx, can_buy)] = profit
        return profit

    return check(0, True)

