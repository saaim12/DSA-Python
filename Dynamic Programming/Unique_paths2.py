"""
Unique Paths II (With Obstacles) in Python 3.12

This file includes:
1. Recursive solution (exponential, not for large grids)
2. Recursive + Memoization (Top-Down DP)
3. Tabulation (Bottom-Up DP)
4. Space-Optimized Tabulation (1D DP)
"""

# ------------------------------
# 1. Recursive solution
# ------------------------------
def unique_paths_obstacle_recursive(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    def check(r, c):
        # Out of bounds or obstacle
        if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
            return 0
        # Start
        if r == 0 and c == 0:
            return 1
        # Recurrence: top + left
        return check(r - 1, c) + check(r, c - 1)

    return check(m - 1, n - 1)


# ------------------------------
# 2. Recursive + Memoization (Top-Down DP)
# ------------------------------
def unique_paths_obstacle_memo(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    memo = {}

    def check(r, c):
        if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
            return 0
        if r == 0 and c == 0:
            return 1
        if (r, c) in memo:
            return memo[(r, c)]
        memo[(r, c)] = check(r - 1, c) + check(r, c - 1)
        return memo[(r, c)]

    return check(m - 1, n - 1)


# ------------------------------
# 3. Tabulation (Bottom-Up DP)
# ------------------------------
def unique_paths_obstacle_tabulation(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0  # obstacle
            elif i == 0 and j == 0:
                dp[i][j] = 1  # start
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[m - 1][n - 1]


# ------------------------------
# 4. Space-Optimized Tabulation (1D DP)
# ------------------------------
def unique_paths_obstacle_space(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [0] * n

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif i == 0 and j == 0:
                dp[j] = 1
            else:
                left = dp[j - 1] if j > 0 else 0
                dp[j] = dp[j] + left

    return dp[n - 1]


# ------------------------------
# Testing all versions
# ------------------------------
if __name__ == "__main__":
    grid1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]  # Expected output: 2

    grid2 = [
        [0, 1],
        [0, 0]
    ]  # Expected output: 1

    print("Recursive:", unique_paths_obstacle_recursive(grid1))
    print("Memoization:", unique_paths_obstacle_memo(grid1))
    print("Tabulation:", unique_paths_obstacle_tabulation(grid1))
    print("Space-Optimized:", unique_paths_obstacle_space(grid1))

    print("Recursive:", unique_paths_obstacle_recursive(grid2))
    print("Memoization:", unique_paths_obstacle_memo(grid2))
    print("Tabulation:", unique_paths_obstacle_tabulation(grid2))
    print("Space-Optimized:", unique_paths_obstacle_space(grid2))
