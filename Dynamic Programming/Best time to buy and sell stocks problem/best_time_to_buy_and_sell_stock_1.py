def buy_and_sell_stock_1(arr):
    max_profit=0
    buy=arr[0]

    for i in range(1,len(arr)):
        cost=arr[i]-buy
        max_profit=max(max_profit,cost)
        buy=min(buy,arr[i])

    return max_profit

print(buy_and_sell_stock_1([7,1,5,3,6,4]))
print(buy_and_sell_stock_1([7,6,4,3,1]))