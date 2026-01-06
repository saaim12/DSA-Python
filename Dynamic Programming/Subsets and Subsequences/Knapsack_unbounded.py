def knapSack(val, wt, W):
    n = len(wt)
    dp = [[-1] * (W + 1) for _ in range(n)]

    def helper(idx, capacity):
        if idx == 0:
            return (capacity // wt[0]) * val[0] if wt[0] <= capacity else 0

        if dp[idx][capacity] != -1:
            return dp[idx][capacity]

        not_pick = helper(idx - 1, capacity)
        pick = 0
        if wt[idx] <= capacity:
            pick = val[idx] + helper(idx, capacity - wt[idx])

        dp[idx][capacity] = max(pick, not_pick)
        return dp[idx][capacity]

    return helper(n - 1, W)
