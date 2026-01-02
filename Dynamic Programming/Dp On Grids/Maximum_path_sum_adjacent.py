arr1 = [[3, 6, 1],
        [2, 3, 4],
        [5, 5, 1]]


# 1️⃣ Recursive solution (exponential)
def maximumPath(arr):
    rows = len(arr)
    cols = len(arr[0])

    def check(r, c):
        if r == rows - 1:
            return arr[r][c]

        # move to adjacent cells in next row
        return arr[r][c] + max(
            check(r + 1, c),  # straight down
            check(r + 1, c - 1) if c > 0 else float('-inf'),  # left diagonal
            check(r + 1, c + 1) if c < cols - 1 else float('-inf')  # right diagonal
        )

    return max(check(0, c) for c in range(cols))


# 2️⃣ Memoized solution (top-down DP)
def maximumPath_with_memo(arr):
    rows = len(arr)
    cols = len(arr[0])
    memo = {}

    def check(r, c):
        if r == rows - 1:
            return arr[r][c]
        if (r, c) in memo:
            return memo[(r, c)]

        maxi = arr[r][c] + max(
            check(r + 1, c),
            check(r + 1, c - 1) if c > 0 else float('-inf'),
            check(r + 1, c + 1) if c < cols - 1 else float('-inf')
        )
        memo[(r, c)] = maxi
        return maxi

    return max(check(0, c) for c in range(cols))


# 3️⃣ Tabulation (bottom-up DP)
def maximumPath_tabulation(arr):
    rows = len(arr)
    cols = len(arr[0])

    dp = [[0] * cols for _ in range(rows)]

    # Base case: last row
    for c in range(cols):
        dp[rows - 1][c] = arr[rows - 1][c]

    # Fill DP from bottom to top
    for r in range(rows - 2, -1, -1):
        for c in range(cols):
            down = dp[r + 1][c]
            left_diag = dp[r + 1][c - 1] if c > 0 else float('-inf')
            right_diag = dp[r + 1][c + 1] if c < cols - 1 else float('-inf')
            dp[r][c] = arr[r][c] + max(down, left_diag, right_diag)

    return max(dp[0])


# 4️⃣ Space-optimized DP
def maximumPath_optimized(arr):
    rows = len(arr)
    cols = len(arr[0])
    prev = arr[-1][:]  # last row

    for r in range(rows - 2, -1, -1):
        curr = [0] * cols
        for c in range(cols):
            down = prev[c]
            left_diag = prev[c - 1] if c > 0 else float('-inf')
            right_diag = prev[c + 1] if c < cols - 1 else float('-inf')
            curr[c] = arr[r][c] + max(down, left_diag, right_diag)
        prev = curr

    return max(prev)


# Testing all
print("Recursive:", maximumPath(arr1))
print("Memoized:", maximumPath_with_memo(arr1))
print("Tabulation:", maximumPath_tabulation(arr1))
print("Optimized:", maximumPath_optimized(arr1))
