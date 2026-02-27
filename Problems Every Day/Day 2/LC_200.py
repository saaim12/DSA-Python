from collections import deque

# ---------------- DFS Version ----------------
def numIslandsDFS(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if grid[i][j] == "0" or (i, j) in visited:
            return

        visited.add((i, j))
        # Explore 4 directions
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == "1":
                dfs(i, j)
                count += 1

    return count

# ---------------- BFS Version ----------------
def numIslandsBFS(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        q = deque([(i, j)])
        visited.add((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                    q.append((nr, nc))
                    visited.add((nr, nc))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == "1":
                bfs(i, j)
                count += 1

    return count

# ---------------- Driver / Test ----------------
if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    print("Number of Islands (DFS):", numIslandsDFS(grid))
    print("Number of Islands (BFS):", numIslandsBFS(grid))