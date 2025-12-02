##########################
# N-Queens Problem
##########################

# Naive Backtracking Solution
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    res = []

    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    board = [["."] * n for _ in range(n)]

    def backtrack(board, row):
        if row == n:
            res.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = "."

    backtrack(board, 0)
    return res

print("Naive N-Queens Solutions (4x4):")
for sol in solveNQueens(4):
    for row in sol:
        print(row)
    print()


# Optimized N-Queens using Sets
def solveNQueensOptimized(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    res = []
    board = [["."] * n for _ in range(n)]
    cols = set()
    diag1 = set()  # row + col (top-right to bottom-left)
    diag2 = set()  # row - col (top-left to bottom-right)

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue

            # Place queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    backtrack(0)
    return res

print("Optimized N-Queens Solutions (4x4):")
for sol in solveNQueensOptimized(4):
    for row in sol:
        print(row)
    print()


##########################
# Sudoku Solver
##########################

# Naive Backtracking Sudoku Solver
def solveSudoku(board):
    """
    Solves a Sudoku board using naive backtracking
    """
    def is_safe(row, col, num):
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        # Check 3x3 sub-box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in map(str, range(1, 10)):
                        if is_safe(row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = "."
                    return False
        return True

    backtrack()
    return board


# Optimized Sudoku Solver using Sets
def solveSudokuOptimized(board):
    """
    Solves a Sudoku board using backtracking + sets for O(1) safety check
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Fill sets with existing numbers
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                box_index = (r // 3) * 3 + (c // 3)
                boxes[box_index].add(num)

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in map(str, range(1, 10)):
                        box_index = (r // 3) * 3 + (c // 3)
                        if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                            board[r][c] = num
                            rows[r].add(num)
                            cols[c].add(num)
                            boxes[box_index].add(num)

                            if backtrack():
                                return True

                            # Backtrack
                            board[r][c] = "."
                            rows[r].remove(num)
                            cols[c].remove(num)
                            boxes[box_index].remove(num)
                    return False
        return True

    backtrack()
    return board


# Example Sudoku Board
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print("Optimized Sudoku Solution:")
solveSudokuOptimized(sudoku_board)
for row in sudoku_board:
    print(row)


## graph coloring problem ####
def graphColoring(V, edges, m):

        # Build adjacency list
    graph = {i: [] for i in range(V)}
    for u, w in edges:
        graph[u].append(w)
        graph[w].append(u)

    color = [0] * V

    def is_safe(node, c):
        for nei in graph[node]:
            if color[nei] == c:
                return False
        return True

    def solve(node):
        if node == V:
             return True

        for c in range(1, m + 1):
            if is_safe(node, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = 0  # backtrack

        return False

    return solve(0)


print(graphColoring(4,[[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]],2))
