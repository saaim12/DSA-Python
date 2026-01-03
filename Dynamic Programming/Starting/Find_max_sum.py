"""
Maximum Sum of Non-Adjacent Elements

Given an array of integers, find the maximum sum of elements such that
no two chosen elements are adjacent.

This file contains:
1. Recursive solution with Memoization (Top-Down DP)
2. Tabulation (Bottom-Up DP)
"""

# =========================================================
# 1️⃣ Recursive + Memoization (Top-Down DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack + memo

def findMaxSum_with_memo(arr):
    """
    Recursive solution with memoization
    """
    memo = {}

    def find(idx):
        # Base cases
        if idx < 0:
            return 0
        if idx == 0:
            return arr[0]

        # Return cached result
        if idx in memo:
            return memo[idx]

        # Option 1: pick current element (then skip previous)
        pick = arr[idx] + find(idx - 2)

        # Option 2: do not pick current element
        not_pick = find(idx - 1)

        # Store the best result
        memo[idx] = max(pick, not_pick)
        return memo[idx]

    return find(len(arr) - 1)


# =========================================================
# 2️⃣ Tabulation (Bottom-Up DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n)

class SolutionTabulation:
    def findMaxSum(self, arr):
        """
        Bottom-up DP solution
        """
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        # dp[i] = maximum sum of non-adjacent elements from arr[0..i]
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            pick = arr[i] + dp[i - 2]  # pick current element
            not_pick = dp[i - 1]       # skip current element
            dp[i] = max(pick, not_pick)

        return dp[n - 1]


# =========================================================
# 3️⃣ Space-Optimized Version
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(1)

class SolutionSpaceOptimized:
    def findMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])

        for i in range(2, n):
            curr = max(arr[i] + prev2, prev1)
            prev2, prev1 = prev1, curr

        return prev1


# =========================================================
# 🔥 Testing All Solutions
# =========================================================

if __name__ == "__main__":
    test_cases = [
        [3, 2, 7, 10],
        [3, 2, 5, 10, 7],
        [5, 5, 10, 100, 10, 5]
    ]

    print("=== Recursive + Memoization ===")
    for arr in test_cases:
        print(f"Array: {arr} -> Max sum: {findMaxSum_with_memo(arr)}")

    print("\n=== Tabulation (Bottom-Up DP) ===")
    solution_tab = SolutionTabulation()
    for arr in test_cases:
        print(f"Array: {arr} -> Max sum: {solution_tab.findMaxSum(arr)}")

    print("\n=== Space-Optimized DP ===")
    solution_opt = SolutionSpaceOptimized()
    for arr in test_cases:
        print(f"Array: {arr} -> Max sum: {solution_opt.findMaxSum(arr)}")
