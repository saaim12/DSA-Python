import heapq
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

    def prims_implementation(self, start):
        visited = set()
        n = len(self.graph)
        mst = []
        pq = [(0, start, -1)]
        paths_sum = 0

        while pq and len(visited) < n:
            wt, node, parent = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            paths_sum += wt

            if parent != -1:
                mst.append((parent, node))

            for nei, w in self.graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (w, nei, node))

        return mst,paths_sum




# Created the graph from image in notes
g = Graph(directed=False)

g.add_edge(0, 1, 2)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 1)
g.add_edge(2, 4, 2)
g.add_edge(2, 3, 2)
g.add_edge(4,3,1)

g.display()

mst = g.prims_implementation(start=0)
print("MST edges:", mst)






