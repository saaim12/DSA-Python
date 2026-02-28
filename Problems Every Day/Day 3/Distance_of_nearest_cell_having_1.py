from collections import deque
def nearest(grid):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[-1 for _ in range(cols)] for _ in range(rows)]


    q = deque([])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0 # the distance to itself is zero

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r,c=q.popleft()
        for dr,dc in directions:
            nr,nc=dr+r,dc+c
            if 0<=nr<rows and 0<=nc<cols and dist[nr][nc]==-1:
                dist[nr][nc]=dist[r][c]+1
                q.append((nr,nc))

    return dist





grid=[[0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]]
print(nearest(grid))
