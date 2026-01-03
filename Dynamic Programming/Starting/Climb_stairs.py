"""
CLIMBING STAIRS PROBLEM
----------------------
You are at the bottom of a staircase with 'n' steps.
You can climb either 1 step or 2 steps at a time.
Return the number of distinct ways to reach the top.
"""

# ======================================================
# 1️⃣ PURE RECURSIVE SOLUTION (BRUTE FORCE)
# ======================================================
# Time Complexity: O(2^n)
# Space Complexity: O(n) - recursion stack
# This solution is NOT efficient but helps understand the problem.

def climb_stairs_recursive(n):
    # Base cases:
    # If n == 0 or n == 1, there is exactly 1 way to climb
    if n <= 1:
        return 1

    # Recursive calls:
    # 1 step + 2 steps
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


# ======================================================
# 2️⃣ RECURSION + MEMOIZATION (TOP-DOWN DP)
# ======================================================
# Time Complexity: O(n)
# Space Complexity: O(n)
# Uses a dictionary to store already computed results

def climb_stairs_memo(n, memo):
    # Base case
    if n <= 1:
        return 1

    # If already computed, return from memo
    if n in memo:
        return memo[n]

    # Store the result in memo before returning
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# ======================================================
# 3️⃣ TABULATION (BOTTOM-UP DP)
# ======================================================
# Time Complexity: O(n)
# Space Complexity: O(n)
# Builds the solution iteratively

def climb_stairs_tabulation(n):
    if n <= 1:
        return 1

    # dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Build dp array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ======================================================
# 4️⃣ SPACE OPTIMIZED DP
# ======================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Best solution for interviews

def climb_stairs_optimized(n):
    if n <= 1:
        return 1

    prev2 = 1  # ways to reach step 0
    prev1 = 1  # ways to reach step 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# ======================================================
# TESTING ALL METHODS
# ======================================================

if __name__ == "__main__":
    n = 3

    print("Recursive:", climb_stairs_recursive(n))
    print("Memoization:", climb_stairs_memo(n, {}))
    print("Tabulation:", climb_stairs_tabulation(n))
    print("Optimized DP:", climb_stairs_optimized(n))
