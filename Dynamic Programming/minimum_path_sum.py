# min_path_sum.py
# Problem: Minimum Path Sum (LeetCode 64)


# -------------------------------
# Memoization (Top-Down DP)
# -------------------------------
def min_path_sum_memo(grid):
    rows = len(grid)
    cols = len(grid[0])
    memo = {}

    def dfs(r, c):
        # out of bounds
        if r >= rows or c >= cols:
            return float('inf')

        # destination
        if r == rows - 1 and c == cols - 1:
            return grid[r][c]

        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = grid[r][c] + min(
            dfs(r + 1, c),    # down
            dfs(r, c + 1)     # right
        )
        return memo[(r, c)]

    return dfs(0, 0)


# -------------------------------
# Tabulation (Bottom-Up DP)
# -------------------------------
def min_path_sum_tabulation(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]


# -------------------------------
# Testing
# -------------------------------
if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print("Memoization:", min_path_sum_memo(grid))      # 7
    print("Tabulation:", min_path_sum_tabulation(grid)) # 7
