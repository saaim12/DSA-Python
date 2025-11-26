import heapq
from collections import deque


class Graph:
    def __init__(self, directed=False):
        # Initialize the graph as a dictionary of adjacency lists
        self.graph = {}
        self.isdirected = directed

    def add_vertex(self, v):
        # Add a vertex if it doesn't exist
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Adds an edge between two vertices.
        Supports both directed and undirected graphs.
        """
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # For directed graphs: only one direction
        if self.isdirected:
            self.graph[vertex1].append((vertex2, weight))
        else:
            # For undirected graphs: add both directions
            self.graph[vertex1].append((vertex2, weight))
            self.graph[vertex2].append((vertex1, weight))

    def display(self):
        # Print adjacency list
        for vertex in self.graph:
            print(f"{vertex} ---> {self.graph[vertex]}")

    ## ---------------- TRAVERSALS ---------------- ##

    def BFS(self, start):
        """
        Breadth-First Search (Level Order Traversal)
        """
        q = deque([start])
        visited = set([start])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node)
                for nei, _ in self.graph[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res.append(level)
        return res

    def DFS(self, start, visited=None, order=None):
        """
        Depth-First Search (Recursive)
        """
        if visited is None:
            visited = set()
        if order is None:
            order = []

        visited.add(start)
        order.append(start)

        for nei, _ in self.graph[start]:
            if nei not in visited:
                self.DFS(nei, visited, order)

        return order

    ## ---------------- CYCLE DETECTION ---------------- ##

    def cycle_un_directed(self, start):
        """
        Detects cycle in an undirected graph using DFS
        """
        visited = set()

        def DFS(node, parent):
            visited.add(node)
            for nei, _ in self.graph[node]:
                if nei not in visited:
                    if DFS(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False

        for v in self.graph:
            if v not in visited:
                if DFS(v, -1):
                    print("Cycle detected (Undirected)")
                    return True
        print("No cycle (Undirected)")
        return False

    def detect_cycle_directed(self):
        """
        Detects cycle in a directed graph using DFS and recursion stack
        """
        visited = set()
        path = set()

        def DFS(node):
            visited.add(node)
            path.add(node)
            for nei, _ in self.graph[node]:
                if nei not in visited:
                    if DFS(nei):
                        return True
                elif nei in path:
                    print("Cycle detected (Directed)")
                    return True
            path.remove(node)
            return False

        for v in self.graph:
            if v not in visited:
                if DFS(v):
                    print("Cycle (Directed)")
                    return True
        print("No cycle (Directed)")
        return False

    ## ---------------- SHORTEST PATHS ---------------- ##

    def shortest_path_in_DAG(self, start):
        """
        Shortest path in a Directed Acyclic Graph using Topological Sort
        """
        visited = set()
        stack = []  # store topological order

        def topo(node):
            visited.add(node)
            for nei, _ in self.graph[node]:
                if nei not in visited:
                    topo(nei)
            stack.append(node)

        # Step 1: Perform Topological Sort
        for v in self.graph:
            if v not in visited:
                topo(v)

        stack.reverse()  # Topological order

        # Step 2: Initialize distances
        dist = {v: float('inf') for v in self.graph}
        dist[start] = 0

        # Step 3: Relax edges in topological order
        for node in stack:
            if dist[node] != float('inf'):
                for nei, weight in self.graph[node]:
                    if dist[node] + weight < dist[nei]:
                        dist[nei] = dist[node] + weight

        print("\nShortest distances from node", start)
        for node in dist:
            print(f"{start} → {node} = {dist[node]}")

        return dist

    def shortes_path_in_undirected_graph_with_unit_weights(self, start):
        """
        Shortest path in an unweighted graph (using BFS)
        """
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        q = deque([start])
        while q:
            node = q.popleft()
            for nei, _ in self.graph[node]:
                if dist[nei] == float('inf'):
                    dist[nei] = dist[node] + 1
                    q.append(nei)
        return dist

    def dijkstra(self, start):
        """
        Dijkstra’s Algorithm for shortest path in weighted graphs
        (Works for non-negative edge weights)
        """
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        min_heap = [(0, start)]  # (distance, node)
        visited = set()

        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            visited.add(node)

            for nei, weight in self.graph[node]:
                if dist[node] + weight < dist[nei]:
                    dist[nei] = dist[node] + weight
                    heapq.heappush(min_heap, (dist[nei], nei))

        print(f"\nDijkstra’s shortest paths from node {start}:")
        for node in dist:
            print(f"{start} → {node} = {dist[node]}")
        return dist


# -------------------- TESTING -------------------- #

# UNDIRECTED GRAPH
g = Graph(directed=False)
g.add_edge(1, 2, 3)
g.add_edge(1, 6, 4)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 6)
g.add_edge(6, 7, 7)
g.add_edge(6, 8, 8)
g.add_edge(4, 5, 9)
g.add_edge(7, 5, 10)

print("\n--- Undirected Graph ---")
g.display()
print("\nBFS:", g.BFS(1))
print("DFS:", g.DFS(1))
g.cycle_un_directed(1)
print("dijkstra ")
g.dijkstra(1)

# DIRECTED GRAPH
g2 = Graph(directed=True)
g2.add_edge(1, 2, 3)
g2.add_edge(1, 6, 4)
g2.add_edge(2, 3, 5)
g2.add_edge(2, 4, 6)
g2.add_edge(6, 7, 7)
g2.add_edge(6, 8, 8)
g2.add_edge(4, 5, 9)
g2.add_edge(7, 5, 10)

print("\n--- Directed Graph ---")
g2.display()
g2.detect_cycle_directed()
g2.shortest_path_in_DAG(1)
