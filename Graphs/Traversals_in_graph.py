import collections
from collections import deque



class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed   # if True → directed graph; if False → undirected

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, w=1):
        """Adds an edge (directed or undirected depending on self.directed flag)."""
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append((v, w))
        if not self.directed:
            # For undirected graphs, add both directions
            self.graph[v].append((u, w))

    def display(self):
        for vertex in self.graph:
            print(vertex, "-->", self.graph[vertex])

    def BFS(self, start):
        queue = deque([start])
        visited = set([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def DFS_iter(self, start):
        visited = set([start])
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return order

    def DFS_recur(self, node, visited=None, order=None):
        if visited is None:
            visited = set()
        if order is None:
            order = []
        if node in visited:
            return order
        order.append(node)
        visited.add(node)
        for neighbor, w in self.graph[node]:
            self.DFS_recur(neighbor, visited, order)
        return order

    def all_path_to_target_DFS(self, target, node, path="", visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        path += node
        if node == target:
            print(path)
        else:
            path += "-->"
            for n, w in self.graph[node]:
                if n not in visited:
                    self.all_path_to_target_DFS(target, n, path, visited)
        visited.remove(node)

    #############################
    # Cycle Detection Functions #
    #############################

    def detect_cycle_directed(self):
        visited=set()
        path=set()
        def DFS(node):
            visited.add(node)
            path.add(node)
            for n,w in self.graph[node]:
                if n not in visited:
                    if DFS(n):

                        return True
                elif n in path:
                    print("cycle detected")
                    return True

            path.remove(node)
            return False

        for v in self.graph:
            if v not in visited:
                if DFS(v):
                    print("cycle")
                    return True
        print("No cycle (Directed)")
        return False



    def detect_cycle_undirected(self):
        visited=set()
        def dfs(node,parent):
            visited.add(node)
            for n,w in self.graph[node]:
                if n not in visited:
                    if dfs(n,node):
                        return True
                elif n!=parent :
                    print("cycle detected")
                    return True

            return False
        for v in self.graph:
            if v not in visited:
                return dfs(v,None)




# -------------------------
# Example Usage
# -------------------------
print("====== UNDIRECTED GRAPH ======")
g1 = Graph(directed=False)
g1.add_edge("1", "2", 5)
g1.add_edge("1", "3", 3)
g1.add_edge("2", "4", 11)
g1.add_edge("3", "5", 8)
g1.add_edge("4", "5", 2)  # uncomment to make a cycle

g1.display()
print("BFS:", g1.BFS("1"))
print("DFS_iter:", g1.DFS_iter("1"))
print("DFS_recur:", g1.DFS_recur("1"))
g1.all_path_to_target_DFS("4", "1")
g1.detect_cycle_undirected()

print("\n====== DIRECTED GRAPH ======")
g2 = Graph(directed=True)
g2.add_edge("1", "2", 5)
g2.add_edge("2", "3", 3)
g2.add_edge("3", "4", 11)
g2.add_edge("4", "5", 8)
g2.add_edge("5", "1", 2)  # creates a cycle

g2.display()
print("BFS:", g2.BFS("1"))
print("DFS_iter:", g2.DFS_iter("1"))
print("DFS_recur:", g2.DFS_recur("1"))
g2.detect_cycle_directed()
