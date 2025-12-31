"""
Problem: Frog Jump (DP)

A frog is standing at stone 0 and wants to reach stone n-1.
The frog can jump either:
1. One step
2. Two steps

Cost of a jump = abs(height[current] - height[previous])

Goal:
Find the minimum total energy required to reach the last stone.
"""


# =========================================================
# 1️⃣ RECURSIVE SOLUTION (Brute Force)
# =========================================================
# Time Complexity: O(2^n)
# Space Complexity: O(n) (recursion stack)

def frog_jump(arr):
    n = len(arr)

    def find(idx):
        # Base case: first stone
        if idx <= 0:
            return 0

        # Jump from previous stone
        left = find(idx - 1) + abs(arr[idx] - arr[idx - 1])

        # Jump from two stones back
        right = float('inf')
        if idx > 1:
            right = find(idx - 2) + abs(arr[idx] - arr[idx - 2])

        return min(left, right)

    return find(n - 1)


print("Recursive:")
print(frog_jump([10, 20, 30, 10]))
print(frog_jump([20, 30, 40]))


# =========================================================
# 2️⃣ MEMOIZATION (Top-Down DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n)

def frog_jump_with_memo(arr):
    n = len(arr)
    memo = {}

    def find(idx):
        # Base case
        if idx <= 0:
            return 0

        # Already computed
        if idx in memo:
            return memo[idx]

        left = find(idx - 1) + abs(arr[idx] - arr[idx - 1])

        right = float('inf')
        if idx > 1:
            right = find(idx - 2) + abs(arr[idx] - arr[idx - 2])

        memo[idx] = min(left, right)
        return memo[idx]

    return find(n - 1)


print("\nMemoization:")
print(frog_jump_with_memo([10, 20, 30, 10]))
print(frog_jump_with_memo([20, 30, 40]))


# =========================================================
# 3️⃣ TABULATION (Bottom-Up DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n)

def frog_jump_with_tabulation(arr):
    n = len(arr)

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(arr[1] - arr[0])

    for i in range(2, n):
        left = dp[i - 1] + abs(arr[i] - arr[i - 1])
        right = dp[i - 2] + abs(arr[i] - arr[i - 2])
        dp[i] = min(left, right)

    return dp[n - 1]


print("\nTabulation:")
print(frog_jump_with_tabulation([10, 20, 30, 10]))
print(frog_jump_with_tabulation([20, 30, 40]))


"""
Recursive      → Simple but slow (TLE for large n)
Memoization    → Optimal and easy to understand
Tabulation     → Best for interviews (iterative + fast)

This problem is equivalent to:
- Climbing stairs with cost
- Fibonacci with constraints
"""


def frog_jump_k(height, k):
    """
    Calculate the minimum cost to reach the last stone,
    where you can jump up to k steps at a time.

    :param height: List[int] - heights of stones
    :param k: int - maximum jump length
    :return: int - minimum total cost
    """
    n = len(height)
    dp = [-1] * n  # Memoization array

    def min_cost(ind):
        # Base case: first stone, cost is 0
        if ind == 0:
            return 0

        # Return cached result
        if dp[ind] != -1:
            return dp[ind]

        # Try all possible jumps from 1 to k
        min_steps = float('inf')
        for j in range(1, k + 1):
            if ind - j >= 0:
                jump_cost = min_cost(ind - j) + abs(height[ind] - height[ind - j])
                min_steps = min(min_steps, jump_cost)

        dp[ind] = min_steps
        return dp[ind]

    # Compute min cost to reach last stone
    return min_cost(n - 1)


# =======================
# Example Usage
# =======================
height = [30, 10, 60, 10, 60, 50]
k = 2
print()
print("-"*50)
print("frog jump with k steps")
print(frog_jump_k(height, k))  # Output: 40
