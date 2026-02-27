# oranges_rotting.py
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        Minimum minutes until no fresh orange remains, else -1
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # Step 1: count fresh oranges and enqueue initial rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        # Step 2: BFS level by level
        minutes = 0
        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # mark as rotten
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1  # increment after processing this level

        return minutes if fresh == 0 else -1

# ---------------- Driver / Test ----------------
if __name__ == "__main__":
    sol = Solution()
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    print("Minutes until all oranges rot:", sol.orangesRotting(grid))