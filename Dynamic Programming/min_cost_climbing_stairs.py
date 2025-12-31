"""
Problem: Min Cost Climbing Stairs

You can start at step 0 or step 1.
You can climb 1 or 2 steps at a time.
Each step has a cost: cost[i].
Goal: reach the top (just after last step) with minimum total cost.

This file contains:
1. Recursive solution with memoization
2. Tabulation (Bottom-up DP)
3. Space-optimized solution
"""

# =========================================================
# 1️⃣ Recursive + Memoization (Top-Down DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack + memo

class SolutionMemo(object):
    def minCostClimbingStairs(self, cost):
        memo = {}
        n = len(cost)

        def find(idx):
            # Base case: you can start at step 0 or 1 at zero cost
            if idx <= 1:
                return 0

            # Return cached result if already computed
            if idx in memo:
                return memo[idx]

            # Either come from idx-1 or idx-2
            one_step = find(idx - 1) + cost[idx - 1]
            two_step = find(idx - 2) + cost[idx - 2]

            memo[idx] = min(one_step, two_step)
            return memo[idx]

        # Start from "top" step
        return find(n)


# =========================================================
# 2️⃣ Tabulation (Bottom-Up DP)
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(n)

class SolutionTabulation(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)  # +1 for "top"

        # Base cases
        dp[0] = 0  # start at step 0
        dp[1] = 0  # start at step 1

        # Fill dp table iteratively
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],  # jump 1 step
                dp[i - 2] + cost[i - 2]   # jump 2 steps
            )

        return dp[n]


# =========================================================
# 3️⃣ Space-Optimized DP
# =========================================================
# Time Complexity: O(n)
# Space Complexity: O(1)

class SolutionSpaceOptimized(object):
    def minCostClimbingStairs(self, cost):
        prev2, prev1 = 0, 0  # dp[0] and dp[1]

        for i in range(2, len(cost) + 1):
            curr = min(
                prev1 + cost[i - 1],  # jump 1 step
                prev2 + cost[i - 2]   # jump 2 steps
            )
            prev2, prev1 = prev1, curr  # shift window

        return prev1


# =========================================================
# 🔥 Testing All Solutions
# =========================================================

if __name__ == "__main__":
    cost_examples = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ]

    print("=== Recursive + Memoization ===")
    solution_memo = SolutionMemo()
    for cost in cost_examples:
        print(f"Cost: {cost} -> Min cost: {solution_memo.minCostClimbingStairs(cost)}")

    print("\n=== Tabulation (Bottom-Up DP) ===")
    solution_tab = SolutionTabulation()
    for cost in cost_examples:
        print(f"Cost: {cost} -> Min cost: {solution_tab.minCostClimbingStairs(cost)}")

    print("\n=== Space-Optimized DP ===")
    solution_opt = SolutionSpaceOptimized()
    for cost in cost_examples:
        print(f"Cost: {cost} -> Min cost: {solution_opt.minCostClimbingStairs(cost)}")
