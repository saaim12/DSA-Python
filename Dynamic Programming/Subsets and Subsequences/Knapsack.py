# ======================================================
# 0/1 Knapsack Problem
# Approaches:
# 1. Recursive
# 2. Memoization (Top-Down DP)
# 3. Tabulation (Bottom-Up DP)
# 4. Space Optimized DP
# ======================================================


# --------------------------
# 1️⃣ Recursive Solution
# --------------------------
def knapsack_recursive(W, wt, val, idx):
    if idx == 0:
        if wt[0] <= W:
            return val[0]
        return 0

    not_pick = knapsack_recursive(W, wt, val, idx - 1)
    pick = 0
    if wt[idx] <= W:
        pick = val[idx] + knapsack_recursive(W - wt[idx], wt, val, idx - 1)

    return max(pick, not_pick)


# --------------------------
# 2️⃣ Memoization (Top-Down)
# --------------------------
def knapsack_memo(W, wt, val):
    n = len(wt)
    dp = [[-1] * (W + 1) for _ in range(n)]

    def helper(idx, capacity):
        if idx == 0:
            if wt[0] <= capacity:
                return val[0]
            return 0

        if dp[idx][capacity] != -1:
            return dp[idx][capacity]

        not_pick = helper(idx - 1, capacity)
        pick = 0
        if wt[idx] <= capacity:
            pick = val[idx] + helper(idx - 1, capacity - wt[idx])

        dp[idx][capacity] = max(pick, not_pick)
        return dp[idx][capacity]

    return helper(n - 1, W)


# --------------------------
# 3️⃣ Tabulation (Bottom-Up)
# --------------------------
def knapsack_tabulation(W, wt, val):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n)]

    # Base case
    for w in range(wt[0], W + 1):
        dp[0][w] = val[0]

    for i in range(1, n):
        for w in range(W + 1):
            not_pick = dp[i - 1][w]
            pick = 0
            if wt[i] <= w:
                pick = val[i] + dp[i - 1][w - wt[i]]
            dp[i][w] = max(pick, not_pick)

    return dp[n - 1][W]


# --------------------------
# 4️⃣ Space Optimized (1D DP)
# --------------------------
def knapsack_optimized(W, wt, val):
    n = len(wt)
    prev = [0] * (W + 1)

    for w in range(wt[0], W + 1):
        prev[w] = val[0]

    for i in range(1, n):
        curr = prev[:]
        for w in range(W + 1):
            if wt[i] <= w:
                curr[w] = max(prev[w], val[i] + prev[w - wt[i]])
        prev = curr

    return prev[W]


# --------------------------
# 5️⃣ Driver Code
# --------------------------
if __name__ == "__main__":
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    W = 7
    n = len(wt)

    print("0/1 Knapsack Results\n")

    print("Recursive        :", knapsack_recursive(W, wt, val, n - 1))
    print("Memoization      :", knapsack_memo(W, wt, val))
    print("Tabulation       :", knapsack_tabulation(W, wt, val))
    print("Space Optimized  :", knapsack_optimized(W, wt, val))
