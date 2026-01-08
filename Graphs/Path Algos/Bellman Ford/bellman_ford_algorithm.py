from math import trunc


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

    #### belllman Ford ###
    def bellman_ford(self,start):
        distances = {v: float('inf') for v in self.graph}
        distances[start] = 0
        ## till N -1 ###
        for _ in range(len(self.graph) - 1):
            for node in self.graph:
                for nei, wt in self.graph[node]:
                    if distances[node] != float('inf') and distances[node] + wt < distances[nei]:
                        distances[nei] = distances[node] + wt
        return distances





    def check_negative_cycle(self,start):
        distances = {v: float('inf') for v in self.graph}
        distances[start] = 0
        for _ in range(len(self.graph)-1):
            for node in self.graph:
                for nei,weight in self.graph[node]:
                    if distances[node]!=float('inf') and distances[node]+weight<distances[nei]:
                        distances[nei]=distances[node]+weight

        ### now if still decreases then break cuz that's a negative cycle ###


        for node in self.graph:
            for nei,weight in self.graph[node]:
                if distances[node]+weight<distances[nei]:
                    print("negative cycle detected")
                    return True

        return False


















# Create a directed graph
g = Graph(directed=True)

# Add all edges as in the picture
g.add_edge(0, 1, 5)
g.add_edge(1, 5, -3)
g.add_edge(1, 2, -2)
g.add_edge(2, 4, 3)
g.add_edge(4, 2, 6)
g.add_edge(5, 3, 1)
g.add_edge(3, 4, -2)

# Display the graph
g.display()
print(g.bellman_ford(0))
g2 = Graph()
g2.add_edge(1, 2, -2)
g2.add_edge(2, 3, -1)
g2.add_edge(3, 1, 2)

print(g2.check_negative_cycle(1))

