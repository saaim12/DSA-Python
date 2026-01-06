# -------------------------
# 1️⃣ Recursive Approach
# -------------------------
def coinChangeRecursive(coins, amount):
    n = len(coins)

    def check(idx, target):
        if target == 0:
            return 0
        if idx == 0:
            if target % coins[0] == 0:
                return target // coins[0]
            else:
                return float('inf')

        not_take = check(idx - 1, target)
        take = float('inf')
        if coins[idx] <= target:
            take = 1 + check(idx, target - coins[idx])

        return min(take, not_take)

    ans = check(n - 1, amount)
    return -1 if ans == float('inf') else ans


# -------------------------
# 2️⃣ Memoization (Top-Down DP)
# -------------------------
def coinChangeMemo(coins, amount):
    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]

    def check(idx, target):
        if target == 0:
            return 0
        if idx == 0:
            if target % coins[0] == 0:
                return target // coins[0]
            else:
                return float('inf')

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_take = check(idx - 1, target)
        take = float('inf')
        if coins[idx] <= target:
            take = 1 + check(idx, target - coins[idx])

        dp[idx][target] = min(take, not_take)
        return dp[idx][target]

    ans = check(n - 1, amount)
    return -1 if ans == float('inf') else ans


# -------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# -------------------------
def coinChangeTabulation(coins, amount):
    n = len(coins)
    INF = float('inf')

    # dp[i][t] = min coins to make sum t using coins[0..i]
    dp = [[INF] * (amount + 1) for _ in range(n)]

    # Base case: only coin[0]
    for t in range(amount + 1):
        if t % coins[0] == 0:
            dp[0][t] = t // coins[0]

    # Fill table
    for i in range(1, n):
        for t in range(amount + 1):
            not_take = dp[i - 1][t]
            take = INF
            if coins[i] <= t:
                take = 1 + dp[i][t - coins[i]]  # unbounded
            dp[i][t] = min(take, not_take)

    ans = dp[n - 1][amount]
    return -1 if ans == INF else ans


# -------------------------
# Test
# -------------------------
coins = [1, 2, 5]
amount = 11

print("Recursive:", coinChangeRecursive(coins, amount))
print("Memoization:", coinChangeMemo(coins, amount))
print("Tabulation:", coinChangeTabulation(coins, amount))
