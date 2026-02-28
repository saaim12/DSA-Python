# surrounded_regions.py

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modify board in-place.
        Capture surrounded regions.
        """

        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # boundary + stop condition
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "#"   # mark as safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Run DFS from boundary O's
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        # Step 2: Flip remaining O → X, and # → O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# ---------------- Driver ----------------
if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]

    sol = Solution()
    sol.solve(board)

    print("Processed Board:")
    for row in board:
        print(row)