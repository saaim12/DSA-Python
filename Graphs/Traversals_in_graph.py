import collections


class graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,vertex,edge,weight):
        if vertex not in self.graph:
            self.add_vertex(vertex)
        if edge not in self.graph:
            self.add_vertex(edge)
        self.graph[edge].append((vertex,weight))
        self.graph[vertex].append((edge,weight))

    def display(self):
        for vertex in self.graph:
            print(vertex, "-->", self.graph[vertex])

    def BFS(self, start):
        queue = collections.deque([start])
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


    def DFS_1(self,start):
        visited=set([start])
        stack=[start]
        order=[]
        while stack:
            node=stack.pop()
            order.append(node)
            for neighbor,weight in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return order
    def DFS_2(self,node,visited,order):
        if node in visited:
            return order

        order.append(node)
        visited.add(node)
        for n,w in self.graph[node]:
            self.DFS_2(n,visited,order)

        return order






g = graph()
g.add_edge("0", "1", 5)
g.add_edge("0", "2", 3)
g.add_edge("1", "3", 7)
g.add_edge("2", "4", 11)
g.add_edge("3", "4", 8)
g.add_edge("3", "5", 2)
g.add_edge("5", "4", 1)
g.add_edge("5", "6", 17)
g.display()
print(g.BFS("0"))
print(g.DFS_1("0"))
print(g.DFS_2("0",set([]),[]))

