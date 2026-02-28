class Solution(object):
    def numEnclaves(self, board):
        """
        Count land cells (1) that cannot reach boundary.
        """

        if not board or not board[0]:
            return 0

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # boundary + stop condition
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 1:
                return

            board[r][c] = -1  # mark as visited boundary land

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Remove boundary-connected land
        for i in range(rows):
            if board[i][0] == 1:
                dfs(i, 0)
            if board[i][cols - 1] == 1:
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == 1:
                dfs(0, j)
            if board[rows - 1][j] == 1:
                dfs(rows - 1, j)

        # Step 2: Count remaining land (true enclaves)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    count += 1
                elif board[i][j] == -1:
                    board[i][j] = 0  # restore

        return count


# ---------------- Driver ----------------
if __name__ == "__main__":
    grid = [
        [0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ]

    sol = Solution()
    print("Number of Enclaves:", sol.numEnclaves(grid))