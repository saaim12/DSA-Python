from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # Undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    # ---------------------------------------------------------
    # BFS Cycle Detection (Undirected Graph)
    # ---------------------------------------------------------
    def has_cycle_bfs(self):
        visited = set()

        for start in range(self.V):
            if start not in visited:
                if self._bfs_detect(start, visited):
                    return True
        return False

    def _bfs_detect(self, start, visited):
        q = deque()
        q.append((start, -1))  # (node, parent)
        visited.add(start)

        while q:
            node, parent = q.popleft()

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, node))
                elif neighbor != parent:
                    return True  # cycle found

        return False

    # ---------------------------------------------------------
    # DFS Cycle Detection (Undirected Graph)
    # ---------------------------------------------------------
    def has_cycle_dfs(self):
        visited = set()

        for node in range(self.V):
            if node not in visited:
                if self._dfs_detect(node, visited, -1):
                    return True
        return False

    def _dfs_detect(self, node, visited, parent):
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self._dfs_detect(neighbor, visited, node):
                    return True
            elif neighbor != parent:
                return True  # cycle found

        return False


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    # Uncomment below to create a cycle
    # g.add_edge(4, 1)

    print("Cycle using BFS:", g.has_cycle_bfs())
    print("Cycle using DFS:", g.has_cycle_dfs())