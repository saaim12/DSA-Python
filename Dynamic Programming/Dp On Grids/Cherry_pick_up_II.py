def cherryPickup(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [-1, 0, 1]  # move left, stay, right
    memo = {}

    def dfs(row, c1, c2):
        # Out of bounds
        if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
            return float('-inf')

        # Base case: last row
        if row == rows - 1:
            if c1 == c2:
                return grid[row][c1]
            else:
                return grid[row][c1] + grid[row][c2]

        if (row, c1, c2) in memo:
            return memo[(row, c1, c2)]

        # Cherries at current row
        cherries = grid[row][c1] if c1 == c2 else grid[row][c1] + grid[row][c2]

        maxi = float('-inf')
        # Move both robots
        for move1 in directions:
            for move2 in directions:
                maxi = max(maxi, cherries + dfs(row + 1, c1 + move1, c2 + move2))

        memo[(row, c1, c2)] = maxi
        return maxi

    return dfs(0, 0, cols - 1)
arr = [[3,1,1],
       [2,5,1],
       [1,5,5],
       [2,1,1]]

print(cherryPickup(arr))  # Output: 24
