# ------------------------------------------
# Partition Equal Subset Problem
# Check if an array can be partitioned into two subsets with equal sum
# Approaches: Recursion, Memoization, Tabulation (DP)
# ------------------------------------------

# --------------------------
# 1. Recursive Approach
# --------------------------
def partition_equal_subset(arr):
    if not arr:
        return False

    total = sum(arr)
    if total % 2 != 0:
        return False  # cannot split odd sum

    target = total // 2
    n = len(arr)

    def check(idx, t):
        if t == 0:
            return True
        if idx < 0:
            return False
        not_take = check(idx - 1, t)
        take = False
        if arr[idx] <= t:
            take = check(idx - 1, t - arr[idx])
        return take or not_take

    return check(n - 1, target)


# --------------------------
# 2. Memoization
# --------------------------
def partition_equal_subset_memo(arr):
    if not arr:
        return False

    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(arr)
    memo = {}

    def check(idx, t):
        if t == 0:
            return True
        if idx < 0:
            return False
        if (idx, t) in memo:
            return memo[(idx, t)]
        not_take = check(idx - 1, t)
        take = False
        if arr[idx] <= t:
            take = check(idx - 1, t - arr[idx])
        memo[(idx, t)] = take or not_take
        return memo[(idx, t)]

    return check(n - 1, target)


# --------------------------
# 3. Tabulation (Bottom-Up DP)
# --------------------------
def partition_equal_subset_tab(arr):
    if not arr:
        return False

    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(arr)

    dp = [[False] * (target + 1) for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][0] = True  # sum 0 always possible
    if arr[0] <= target:
        dp[0][arr[0]] = True

    # Fill DP table
    for i in range(1, n):
        for t in range(1, target + 1):
            not_take = dp[i - 1][t]
            take = False
            if arr[i] <= t:
                take = dp[i - 1][t - arr[i]]
            dp[i][t] = not_take or take

    return dp[n - 1][target]

def partition_sum_k_fully_optimized(arr):
    if not arr:
        return False

    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(arr)

    prev = [False] * (target + 1)
    prev[0] = True

    if arr[0] <= target:
        prev[arr[0]] = True

    for i in range(1, n):
        curr = prev[:]
        for t in range(target + 1):
            if arr[i] <= t:
                curr[t] = prev[t] or prev[t - arr[i]]
        prev = curr

    return prev[target]


# --------------------------
# 4. Driver / Test Cases
# --------------------------
if __name__ == "__main__":
    test_cases = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [3, 1, 1, 2, 2, 1],
        [2, 2, 3, 5]
    ]

    methods = [
        ("Recursive", partition_equal_subset),
        ("Memoization", partition_equal_subset_memo),
        ("Tabulation", partition_equal_subset_tab)
    ]

    for arr in test_cases:
        print(f"\nArray: {arr}")
        for name, func in methods:
            result = func(arr)
            print(f"{name:12}: {result}")
