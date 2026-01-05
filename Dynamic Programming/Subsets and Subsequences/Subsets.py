# ------------------------------------------
# Subset Sum Problem: Check if sum = target
# Methods: Recursion, Memoization, Tabulation, Space Optimized
# ------------------------------------------

# --------------------------
# 1. Recursive approach
# --------------------------
def subset_sum_recursive(arr, target):
    def check(idx, t):
        if t == 0:  # sum 0 always possible
            return True
        if idx == 0:  # only first element available
            return arr[0] == t
        not_pick = check(idx - 1, t)
        pick = False
        if arr[idx] <= t:
            pick = check(idx - 1, t - arr[idx])
        return pick or not_pick

    return check(len(arr) - 1, target)


# --------------------------
# 2. Memoization
# --------------------------
def subset_sum_memo(arr, target):
    memo = {}

    def check(idx, t):
        if t == 0:
            return True
        if idx == 0:
            return arr[0] == t
        if (idx, t) in memo:
            return memo[(idx, t)]

        not_pick = check(idx - 1, t)
        pick = False
        if arr[idx] <= t:
            pick = check(idx - 1, t - arr[idx])
        memo[(idx, t)] = pick or not_pick
        return memo[(idx, t)]

    return check(len(arr) - 1, target)


# --------------------------
# 3. Tabulation (Bottom-Up DP)
# --------------------------
def subset_sum_tabulation(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][0] = True  # sum 0 always possible
    if arr[0] <= target:
        dp[0][arr[0]] = True

    # Fill the DP table
    for i in range(1, n):
        for j in range(1, target + 1):
            not_pick = dp[i - 1][j]
            pick = False
            if j >= arr[i]:
                pick = dp[i - 1][j - arr[i]]
            dp[i][j] = pick or not_pick

    return dp[n - 1][target]


# --------------------------
# 4. Space-Optimized DP
# --------------------------
def subset_sum_space_optimized(arr, target):
    n = len(arr)
    prev = [False] * (target + 1)

    # Base cases
    prev[0] = True
    if arr[0] <= target:
        prev[arr[0]] = True

    for i in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True  # sum 0 always possible
        for j in range(1, target + 1):
            not_pick = prev[j]
            pick = False
            if j >= arr[i]:
                pick = prev[j - arr[i]]
            curr[j] = pick or not_pick
        prev = curr

    return prev[target]


# --------------------------
# 5. Driver / Test Cases
# --------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 3),
        ([2, 4, 6], 5),
        ([3, 34, 4, 12, 5, 2], 9),
        ([1, 1, 1, 1], 2)
    ]

    methods = [
        ("Recursive", subset_sum_recursive),
        ("Memoization", subset_sum_memo),
        ("Tabulation", subset_sum_tabulation),
        ("Space Optimized", subset_sum_space_optimized)
    ]

    for arr, target in test_cases:
        print(f"\nArray: {arr}, Target: {target}")
        for name, func in methods:
            result = func(arr, target)
            print(f"{name:17}: {result}")
