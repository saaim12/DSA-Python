from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # Directed edge u → v
        self.graph[u].append(v)

    # ---------------------------------------------------------
    # 1️⃣ Cycle Detection Using DFS (Recursion Stack)
    # ---------------------------------------------------------
    def has_cycle_dfs(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in range(self.V):
            if node not in visited:
                if dfs(node):
                    return True

        return False

    # ---------------------------------------------------------
    # 2️⃣ Cycle Detection Using Kahn's Algorithm (BFS)
    # ---------------------------------------------------------
    def has_cycle_kahn(self):
        indegree = [0] * self.V

        # Compute indegree
        for u in range(self.V):
            for v in self.graph[u]:
                indegree[v] += 1

        # Queue all nodes with indegree 0
        q = deque()
        for i in range(self.V):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            node = q.popleft()
            count += 1

            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If all nodes processed → no cycle
        return count != self.V


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------
if __name__ == "__main__":
    g = Graph(4)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    # Uncomment below to create a cycle
    # g.add_edge(3, 1)

    print("Cycle using DFS:", g.has_cycle_dfs())
    print("Cycle using Kahn:", g.has_cycle_kahn())