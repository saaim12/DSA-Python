import collections
import heapq



class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge, weight):
        if vertex not in self.graph:
            self.add_vertex(vertex)
        if edge not in self.graph:
            self.add_vertex(edge)
        self.graph[vertex].append((edge, weight))
        self.graph[edge].append((vertex, weight))  # undirected

    def bfs(self, start):
        queue = collections.deque([start])
        visited = set()
        order = []  # to record traversal order

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor, weight in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order
    def dfs_iterative(self,start):
        stack=[start]
        visited=set()
        order=[]
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
            for neighbor,weight in reversed(self.graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
        return order
    def dfs_recursive(self,start,visited):
        if start in visited:
            return visited
        visited.add(start)

        for n,w in self.graph[start]:
            self.dfs_recursive(n,visited)
        return visited

    def different_paths(self, path, start, target, visited=None):
        if visited is None:
            visited = set()

        # mark current node as visited
        visited.add(start)

        # add current node to path (string concatenation)
        path = path + str(start) + " "

        # if we reached the target, print the path
        if start == target:
            print(path.strip())
            return
        else:
            # explore neighbors
            for n, w in self.graph[start]:
                if n not in visited:  # avoid going back
                    self.different_paths(path, n, target, visited.copy())

    def display(self):
        for vertex in self.graph:
            print(vertex, "-->", self.graph[vertex])

    def cycle_detection_in_undirected_graph(self):
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for n, w in self.graph[node]:
                if n not in visited:
                    if dfs(n, node):  # recurse deeper
                        return True
                elif n != parent:  # if visited and not coming from parent → cycle
                    return True
            return False

        # check every connected component
        for node in self.graph:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False

    def cycle_detection_in_directed_graph(self):
        visited = set()
        recStack = set()

        def dfs(node):
            visited.add(node)
            recStack.add(node)

            for n, w in self.graph[node]:
                if n not in visited:
                    if dfs(n):
                        return True
                elif n in recStack:  # cycle detected
                    return True

            recStack.remove(node)  # backtrack
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False

    def diskstra(self,start):
        heap = [(0, start)] # cuz from start to start distance is zero
        distances = {node: float('inf') for node in self.graph} # making a dict and adding -int as a temp distance for every node
        distances[start] = 0 # start distance is zero
        while heap:
            dist,node=heapq.heappop(heap)
            if dist > distances[node]:
                continue
            for nei, w in self.graph[node]:
                new_dist = dist + w
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        return distances

    def bellmanford(self,start):
        distances = {node: float('inf') for node in self.graph}  # making a dict and adding -int as a temp distance for every node
        distances[start] = 0
        vertices = len(self.graph)
        for _ in range(vertices - 1):
            for u in self.graph:
                for v, w in self.graph[u]:
                    if distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w

        # Step 3: Check for negative weight cycles
        for u in self.graph:
            for v, w in self.graph[u]:
                if distances[u] + w < distances[v]:
                    print("Graph contains negative weight cycle")
                    return None
        return distances

    def prims(self, start):
        visited = set()
        mst_edges = []   # store edges in MST
        total_weight = 0

        # Min-heap → (weight, current_node, neighbor)
        heap = [(0, start, None)]

        while heap:
            weight, node, parent = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            if parent is not None:  # avoid adding the very first dummy edge
                mst_edges.append((parent, node, weight))
                total_weight += weight

            for neighbor, w in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (w, neighbor, node))

        return mst_edges, total_weight





# Example usage
g = Graph()
g.add_edge("0", "1", 5)
g.add_edge("0", "2", 3)
g.add_edge("1", "3", 7)
g.add_edge("2", "4", 11)
g.add_edge("3", "4", 8)
g.add_edge("3", "5", 2)
g.add_edge("5", "4", 1)
g.add_edge("5", "6", 17)
g2 = Graph()
g2.add_edge("0", "1", 1)
g2.add_edge("0", "2", 1)
g2.add_edge("2", "3", 1)
g2.add_edge("2", "4", 1)

g.display()

print(g.bfs("0"))
print(g.dfs_iterative("0"))
print(g.dfs_recursive("0",set()))
print(g.different_paths("","0","5"))
g2.display()
print("Cycle Exists?", g2.cycle_detection_in_undirected_graph())
g2.display()
print(g.diskstra("0"))
print(g.bellmanford("0"))