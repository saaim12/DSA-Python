# ========================================================
# Count Subset & Partition Problems
# Includes:
# 1. Count subsets with sum K
# 2. Count partitions with given difference D
# Approaches: Recursive, Memoization, Tabulation, Space-Optimized
# ========================================================

# --------------------------
# 1️⃣ Count subsets with sum K
# --------------------------

def count_subsets_with_sum_k(arr, k):
    n = len(arr)
    memo = {}

    def helper(idx, target):
        if idx == 0:
            if target == 0 and arr[0] == 0:
                return 2
            if target == 0 or arr[0] == target:
                return 1
            return 0

        if (idx, target) in memo:
            return memo[(idx, target)]

        not_take = helper(idx - 1, target)
        take = 0
        if arr[idx] <= target:
            take = helper(idx - 1, target - arr[idx])

        memo[(idx, target)] = take + not_take
        return memo[(idx, target)]

    return helper(n - 1, k)


def count_subsets_with_sum_k_tab(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case
    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= k:
        dp[0][arr[0]] = 1

    # Fill DP table
    for i in range(1, n):
        for t in range(k + 1):
            not_take = dp[i - 1][t]
            take = 0
            if arr[i] <= t:
                take = dp[i - 1][t - arr[i]]
            dp[i][t] = take + not_take

    return dp[n - 1][k]


def count_subsets_with_sum_k_optimized(arr, k):
    n = len(arr)
    prev = [0] * (k + 1)

    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1

    if arr[0] != 0 and arr[0] <= k:
        prev[arr[0]] = 1

    for i in range(1, n):
        curr = [0] * (k + 1)
        for t in range(k + 1):
            not_take = prev[t]
            take = 0
            if arr[i] <= t:
                take = prev[t - arr[i]]
            curr[t] = take + not_take
        prev = curr

    return prev[k]


# --------------------------
# 2️⃣ Count partitions with given difference D
# --------------------------

def count_partitions_with_diff(arr, D):
    total = sum(arr)
    if (total + D) % 2 != 0 or total < D:
        return 0

    target = (total + D) // 2
    return count_subsets_with_sum_k(arr, target)


def count_partitions_with_diff_tab(arr, D):
    total = sum(arr)
    if (total + D) % 2 != 0 or total < D:
        return 0

    target = (total + D) // 2
    return count_subsets_with_sum_k_tab(arr, target)


def count_partitions_with_diff_optimized(arr, D):
    total = sum(arr)
    if (total + D) % 2 != 0 or total < D:
        return 0

    target = (total + D) // 2
    return count_subsets_with_sum_k_optimized(arr, target)


# --------------------------
# 3️⃣ Driver / Test Cases
# --------------------------

if __name__ == "__main__":
    print("===== Count Subsets with Sum K =====")
    test_cases_subsets = [
        ([1, 2, 3], 3),
        ([0, 0, 1], 1),
        ([1, 1, 1, 1], 2)
    ]

    for arr, k in test_cases_subsets:
        print(f"\nArray: {arr}, K = {k}")
        print("Recursive + Memo:", count_subsets_with_sum_k(arr, k))
        print("Tabulation      :", count_subsets_with_sum_k_tab(arr, k))
        print("Optimized       :", count_subsets_with_sum_k_optimized(arr, k))

    print("\n===== Count Partitions with Difference D =====")
    test_cases_partition = [
        ([1, 1, 2, 3], 1),
        ([1, 5, 11, 5], 1),
        ([3, 1, 1, 2, 2, 1], 1),
        ([2, 2, 3, 5], 1)
    ]

    for arr, D in test_cases_partition:
        print(f"\nArray: {arr}, D = {D}")
        print("Recursive + Memo:", count_partitions_with_diff(arr, D))
        print("Tabulation      :", count_partitions_with_diff_tab(arr, D))
        print("Optimized       :", count_partitions_with_diff_optimized(arr, D))
