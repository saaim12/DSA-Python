"""
====================================================
HOUSE ROBBER DP PATTERNS
====================================================

Problems Covered:
1) House Robber I  (Linear houses)
2) House Robber II (Circular houses)

For EACH problem:
- Memoization (Top-down DP)
- Tabulation (Bottom-up DP)
- Space Optimized (Best approach)

====================================================
"""

# ==================================================
# HOUSE ROBBER I (Linear Houses)
# ==================================================

# ---------- 1) MEMOIZATION ----------
def house_robber_memo(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n) -> recursion + memo
    """
    memo = {}

    def dfs(i):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]
        if i in memo:
            return memo[i]

        pick = nums[i] + dfs(i - 2)
        not_pick = dfs(i - 1)

        memo[i] = max(pick, not_pick)
        return memo[i]

    return dfs(len(nums) - 1)


# ---------- 2) TABULATION ----------
def house_robber_tabulation(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


# ---------- 3) SPACE OPTIMIZED ----------
def house_robber_optimized(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev1 = 0  # dp[i-2]
    prev2 = 0  # dp[i-1]

    for num in nums:
        curr = max(prev1 + num, prev2)
        prev1 = prev2
        prev2 = curr

    return prev2


# ==================================================
# HOUSE ROBBER II (Circular Houses)
# ==================================================
"""
Key idea:
- You CANNOT rob first and last together
- So solve two cases:
    1) Exclude last house
    2) Exclude first house
- Take max of both
"""


# ---------- 1) MEMOIZATION ----------
def house_robber_2_memo(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(arr):
        memo = {}

        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            if i in memo:
                return memo[i]

            memo[i] = max(arr[i] + dfs(i - 2), dfs(i - 1))
            return memo[i]

        return dfs(len(arr) - 1)

    return max(
        rob_linear(nums[:-1]),  # exclude last
        rob_linear(nums[1:])    # exclude first
    )


# ---------- 2) TABULATION ----------
def house_robber_2_tabulation(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(arr):
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )


# ---------- 3) SPACE OPTIMIZED ----------
def house_robber_2_optimized(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(arr):
        prev1 = 0
        prev2 = 0
        for num in arr:
            curr = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = curr
        return prev2

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )


# ==================================================
# DRIVER CODE (Testing)
# ==================================================
if __name__ == "__main__":

    nums1 = [2, 7, 9, 3, 1]
    nums2 = [2, 3, 2]

    print("HOUSE ROBBER I")
    print("Memo:", house_robber_memo(nums1))
    print("Tabulation:", house_robber_tabulation(nums1))
    print("Optimized:", house_robber_optimized(nums1))

    print("\nHOUSE ROBBER II")
    print("Memo:", house_robber_2_memo(nums2))
    print("Tabulation:", house_robber_2_tabulation(nums2))
    print("Optimized:", house_robber_2_optimized(nums2))
