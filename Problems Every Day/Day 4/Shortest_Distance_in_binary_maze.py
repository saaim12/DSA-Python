import heapq
from collections import deque

class Solution:
    def shortestPath(self, grid, source, destination):
        rows = len(grid)
        cols = len(grid[0])
        sr, sc = source
        ds_r, ds_c = destination
        # invalid case
        if grid[sr][sc] ==0 or grid[ds_r][ds_c]==0:
            return -1

        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        q=deque([(0,sr,sc)])
        visited=set()
        visited.add((sr,sc))
        while q:
            dist,r,c=q.popleft()
            if r==ds_r and c==ds_c:
                return dist

            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                    q.append((dist+1,nr,nc))
                    visited.add((nr,nc))


        return -1

















grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]

S=Solution()
print(S.shortestPath(grid,(0,1),(2,2)))