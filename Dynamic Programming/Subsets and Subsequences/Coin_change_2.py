# ---------------------------------------------
# Coin Change II - Number of Ways to Make Amount
# ---------------------------------------------

# -------------------------
# 1️⃣ Recursive Approach
# -------------------------
def coinChangeRecursive(coins, amount):
    n = len(coins)

    def check(idx, target):
        if target == 0:
            return 1  # one valid way
        if idx == 0:
            return 1 if target % coins[0] == 0 else 0

        not_take = check(idx - 1, target)
        take = 0
        if coins[idx] <= target:
            take = check(idx, target - coins[idx])  # unbounded

        return take + not_take

    return check(n - 1, amount)


# -------------------------
# 2️⃣ Memoization (Top-Down DP)
# -------------------------
def coinChangeMemo(coins, amount):
    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]

    def check(idx, target):
        if target == 0:
            return 1
        if idx == 0:
            return 1 if target % coins[0] == 0 else 0

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_take = check(idx - 1, target)
        take = 0
        if coins[idx] <= target:
            take = check(idx, target - coins[idx])

        dp[idx][target] = take + not_take
        return dp[idx][target]

    return check(n - 1, amount)


# -------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# -------------------------
def coinChangeTabulation(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    # Base case: only coin[0]
    for t in range(amount + 1):
        if t % coins[0] == 0:
            dp[0][t] = 1

    # Fill table
    for i in range(1, n):
        for t in range(amount + 1):
            not_take = dp[i - 1][t]
            take = 0
            if coins[i] <= t:
                take = dp[i][t - coins[i]]  # unbounded
            dp[i][t] = take + not_take

    return dp[n - 1][amount]


# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    coins_list = [
        ([1, 2, 5], 5),
        ([2, 3, 7], 7),
        ([1, 2, 3], 4),
        ([1], 10)
    ]

    for coins, amount in coins_list:
        print(f"Coins: {coins}, Amount: {amount}")
        print("Recursive:", coinChangeRecursive(coins, amount))
        print("Memoization:", coinChangeMemo(coins, amount))
        print("Tabulation:", coinChangeTabulation(coins, amount))
        print("-" * 40)
