"""
Unique Paths Problems in Python 3.12

This file includes:
1. Recursive solution
2. Recursive + Memoization (Top-Down DP)
3. Tabulation (Bottom-Up DP)
4. Space-Optimized Tabulation (1D DP)
"""


# ------------------------------
# 1. Recursive solution (exponential)
# ------------------------------
def unique_paths(m, n):
    def check(r, c):
        # Base case: reached start
        if r == 0 and c == 0:
            return 1
        # Out of bounds
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        # Recurrence: top + left
        return check(r - 1, c) + check(r, c - 1)

    return check(m - 1, n - 1)


# ------------------------------
# 2. Recursive + Memoization (Top-Down DP)
# ------------------------------
def unique_paths_with_memo(m, n):
    memo = {}

    def check(r, c):
        # Base case: start
        if r == 0 and c == 0:
            memo[(r, c)] = 1
            return 1
        # Out of bounds
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        # Return memoized value if exists
        if (r, c) in memo:
            return memo[(r, c)]
        # Recurrence: top + left
        memo[(r, c)] = check(r - 1, c) + check(r, c - 1)
        return memo[(r, c)]

    return check(m - 1, n - 1)


# ------------------------------
# 3. Tabulation (Bottom-Up DP)
# ------------------------------
def unique_paths_with_tabulation(m, n):
    # Create DP table
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1  # start
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[m - 1][n - 1]


# ------------------------------
# 4. Space-Optimized Tabulation (1D DP)
# ------------------------------
def unique_path_most_optimized(m, n):
    # Only store current row
    dp = [1] * n  # first row all 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]  # top + left

    return dp[n - 1]


# ------------------------------
# Testing all versions
# ------------------------------
if __name__ == "__main__":
    print("Recursive:", unique_paths(3, 2))  # 3
    print("Recursive:", unique_paths(3, 7))  # 28

    print("Memoization:", unique_paths_with_memo(3, 2))  # 3
    print("Memoization:", unique_paths_with_memo(3, 7))  # 28

    print("Tabulation:", unique_paths_with_tabulation(3, 2))  # 3
    print("Tabulation:", unique_paths_with_tabulation(3, 7))  # 28

    print("Space-Optimized:", unique_path_most_optimized(3, 2))  # 3
    print("Space-Optimized:", unique_path_most_optimized(3, 7))  # 28


def unique_path_most_optimized(m,n):
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]



