def minimumDifference(arr):
    total = sum(arr)
    n = len(arr)

    dp = [[False] * (total + 1) for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][0] = True  # sum 0 is always possible
    if arr[0] <= total:
        dp[0][arr[0]] = True  # take first element if possible

    # Fill DP table
    for i in range(1, n):
        for t in range(1, total + 1):
            not_take = dp[i - 1][t]
            take = False
            if arr[i] <= t:
                take = dp[i - 1][t - arr[i]]
            dp[i][t] = not_take or take

    target = total // 2
    mini = float('inf')
    for s in range(target):
        if dp[n - 1][s] == True:
            mini = min(mini, abs(total - s) - s)
    return mini


print((minimumDifference([3,9,7,3])))