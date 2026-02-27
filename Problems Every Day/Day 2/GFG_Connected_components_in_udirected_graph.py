# connected_components_bfs.py
from collections import deque

class Solution:
    def getComponents(self, V, edges):
        """
        Returns all connected components of a graph as lists of nodes.
        BFS implemented in two styles:
        1. Add node when popping (classic)
        2. Add node when enqueueing (eager)
        """
        # Build adjacency list
        graph = {i: [] for i in range(V)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected graph

        # ---------------- BFS: Add when popping ----------------
        def bfs_pop(start, visited):
            level = set()
            q = deque([start])
            visited.add(start)
            while q:
                node = q.popleft()
                level.add(node)  # add when popping
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return list(level)

        # ---------------- BFS: Add when enqueueing ----------------
        def bfs_enqueue(start, visited):
            level = set()
            q = deque([start])
            visited.add(start)
            level.add(start)  # add when enqueueing
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        level.add(nei)  # add here
                        q.append(nei)
            return list(level)

        # Using BFS "add when popping"
        visited1 = set()
        components_pop = []
        for i in range(V):
            if i not in visited1:
                comp = bfs_pop(i, visited1)
                components_pop.append(comp)

        # Using BFS "add when enqueueing"
        visited2 = set()
        components_enqueue = []
        for i in range(V):
            if i not in visited2:
                comp = bfs_enqueue(i, visited2)
                components_enqueue.append(comp)

        return components_pop, components_enqueue

# ---------------- Driver / Test ----------------
if __name__ == "__main__":
    sol = Solution()
    V = 6
    edges = [[0,1],[0,2],[3,4],[4,5]]

    components_pop, components_enqueue = sol.getComponents(V, edges)

    print("BFS Add When Popping:", components_pop)
    print("BFS Add When Enqueueing:", components_enqueue)