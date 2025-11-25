import heapq
from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.is_directed = directed

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, w=1):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)

        # Add edge
        self.graph[v1].append((v2, w))

        # If undirected, add reverse edge
        if not self.is_directed:
            self.graph[v2].append((v1, w))

    def display(self):
        print("\nGraph:")
        for v in self.graph:
            print(f"{v}  -->  {self.graph[v]}")
        print()

    # -------------------------------------------------------------
    # Dijkstra Algorithm
    # -------------------------------------------------------------
    def dijkstra(self, start):
        distances = {i: float('inf') for i in self.graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            dist, node = heapq.heappop(pq)

            if dist > distances[node]:
                continue

            for nei, w in self.graph[node]:
                new_dist = dist + w
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        return distances

    # -------------------------------------------------------------
    # Pretty Print Matrix
    # -------------------------------------------------------------
    def print_matrix(self, mat, title="Matrix"):
        print(f"\n{title}:")
        for row in mat:
            print("  ".join(f"{x:3}" if x != float('inf') else "inf" for x in row))
        print()

    # -------------------------------------------------------------
    # BFS shortest path in binary maze
    # -------------------------------------------------------------
    def shortest_binary_maze(self, grid, start, dst):
        rows, cols = len(grid), len(grid[0])
        maze = [[float('inf')] * cols for _ in range(rows)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        sr, sc = start
        dr, dc = dst

        maze[sr][sc] = 0
        q = deque([(sr, sc, 0)])
        visited = {(sr, sc)}

        while q:
            r, c, d = q.popleft()

            if (r, c) == (dr, dc):
                self.print_matrix(maze, "Final Distance Matrix")
                return d

            for dr2, dc2 in directions:
                nr, nc = r + dr2, c + dc2

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        maze[nr][nc] = d + 1
                        q.append((nr, nc, d + 1))

        self.print_matrix(maze, "Unreachable Distance Matrix")
        return -1

    # -------------------------------------------------------------
    # Path With Minimum Effort (Dijkstra variant)
    # -------------------------------------------------------------
    def min_effort_path(self, start, grid, dest):
        rows, cols = len(grid), len(grid[0])
        sr, sc = start
        dr, dc = dest

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[sr][sc] = 0

        pq = [(0, sr, sc)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        iteration = 0

        print("\n--- Running Minimum Effort Path ---")

        while pq:
            curr_eff, r, c = heapq.heappop(pq)

            print(f"\nIteration {iteration}")
            print(f"Current cell: ({r},{c})  |  Effort = {curr_eff}")

            if curr_eff > efforts[r][c]:
                print(" → Skipping outdated state")
                iteration += 1
                continue

            if (r, c) == (dr, dc):
                print("\nReached destination!")
                self.print_matrix(efforts, "Final Effort Matrix")
                return curr_eff

            for dr2, dc2 in directions:
                nr, nc = r + dr2, c + dc2

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(curr_eff, abs(grid[nr][nc] - grid[r][c]))
                    print(f"  Checking neighbor ({nr},{nc}) → New effort = {new_effort}")

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
                        print("  → Updated & pushed to heap")

            self.print_matrix(efforts, "Effort Matrix (current)")
            iteration += 1

        self.print_matrix(efforts, "Effort Matrix (end)")
        return efforts[dr][dc]

    def cheapest_flight(self,grid):
        #first make graph





g = Graph(directed=False)
g.add_edge(0, 2, 4)
g.add_edge(0, 1, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 4, 1)
g.add_edge(2, 5, 6)
g.add_edge(3, 5, 2)
g.add_edge(4, 5, 3)

print("\nDijkstra result:", g.dijkstra(0))
g.display()

grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 0, 0, 1]
]

print("Shortest path in binary maze:",
      g.shortest_binary_maze(grid, (0,1), (2,2)))

#print("Minimum effort path:", g.min_effort_path((0,0), [[1,2,2],[3,8,2],[5,3,5]], (2,2)))
