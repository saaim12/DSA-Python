from collections import deque


class graph:
    def __init__(self,directed=False):
        self.graph={}
        self.isdirected=directed
    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]

    def add_edge(self,vertex1,vertex2,weight=1):
        """Adds an edge (directed or undirected depending on self.directed flag)."""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        if self.isdirected:
            self.graph[vertex1].append((vertex2,weight))
        if not self.isdirected:
            self.graph[vertex1].append((vertex2,weight))
            self.graph[vertex2].append((vertex1, weight))

    def display(self):
        for vertex in self.graph:
            print(str(vertex) + " ---> "+str(self.graph[vertex]))


    ## TRAVERSALS ##

    def BFS(self,start):
        q=deque([start])
        visited=set([start])
        res=[]

        while q:
            level=[]
            for _ in range(len(q)):
                n=q.popleft()
                level.append(n)
                for n,w in self.graph[n]:
                    if n not in visited:
                       q.append(n)
                       visited.add(n)
            res.append(level)


        return res
    def DFS(self,start,visited=None,order=None):
        if visited is None:
            visited=set([])
        if order is None:
            order=[]
        visited.add(start)
        order.append(start)
        for n,w in self.graph[start]:
            if n not in visited:
                self.DFS(n,visited,order)

        return order
  ####   cycle Detection #####
    def cycle_un_directed(self,start):
        visited=set()
        def DFS(node,parent):
            visited.add(node)
            for n,w in self.graph[node]:
                if n not in visited:
                        if DFS(n,node):
                           return True
                elif n!=parent:
                    return True
            return False

        for v in self.graph:
            if v not in visited:
                if DFS(v, -1):
                    return True
        return False





g=graph(directed=False)
g.add_edge(1,2,3)
g.add_edge(1,6,4)
g.add_edge(2,3,5)
g.add_edge(2,4,6)
g.add_edge(6,7,7)
g.add_edge(6,8,8)
g.add_edge(4,5,9)
g.add_edge(7,5,10)
g.display()
print(g.BFS(1))
print(g.cycle_un_directed(1))
g2 = graph(directed=True)
g2.add_edge(1,2,3)
g2.add_edge(1,6,4)
g2.add_edge(2,3,5)
g2.add_edge(2,4,6)
g2.add_edge(6,7,7)
g2.add_edge(6,8,8)
g2.add_edge(4,5,9)
g2.add_edge(7,5,10)

g.display()
print("\nBFS (starting from 1):", g.BFS(1))
print("\nDFS (starting from 1):", g.DFS(1,None,None))



