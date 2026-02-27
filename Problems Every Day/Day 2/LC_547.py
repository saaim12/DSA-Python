# provinces.py
from collections import deque

# ---------------- BFS Version ----------------
def number_of_provinces_bfs(isConnected):
    """
    Count number of provinces using BFS
    :param isConnected: List[List[int]] adjacency matrix
    :return: int number of provinces
    """
    n = len(isConnected)
    # Build graph (adjacency list) from matrix
    graph = {i: [j for j in range(n) if i != j and isConnected[i][j] == 1] for i in range(n)}
    visited = set()
    provinces = 0

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

    for i in range(n):
        if i not in visited:
            bfs(i)
            provinces += 1

    return provinces

# ---------------- DFS Version ----------------
def number_of_provinces_dfs(isConnected):
    """
    Count number of provinces using DFS
    :param isConnected: List[List[int]] adjacency matrix
    :return: int number of provinces
    """
    n = len(isConnected)
    graph = {i: [j for j in range(n) if i != j and isConnected[i][j] == 1] for i in range(n)}
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count

# ---------------- Driver / Test ----------------
if __name__ == "__main__":
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]

    print("Number of provinces (BFS):", number_of_provinces_bfs(isConnected))
    print("Number of provinces (DFS):", number_of_provinces_dfs(isConnected))