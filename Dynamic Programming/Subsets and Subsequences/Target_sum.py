def findTargetSumWays(arr, target):
    n = len(arr)
    dp = {}

    def check(idx, t):
        if idx < 0:
            return 1 if t == 0 else 0
        if (idx, t) in dp:
            return dp[(idx, t)]

        not_take = check(idx - 1, t + arr[idx])
        take = check(idx - 1, t - arr[idx])

        dp[(idx, t)] = take + not_take
        return dp[(idx, t)]

    return check(n - 1, target)
