import heapq
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

    def shortest_path_in_DAG(self, start):
        visited = set()
        stack = []  # store topological order

        def topo(node):
            visited.add(node)
            for nei, w in self.graph[node]:
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

    def shortes_path_in_undirected_graph_with_unit_weights(self,start):
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        q=deque([start])
        while q :
            n,w=q.popleft()
            for nei in self.graph[n]:
                if dist[nei] ==float('inf'):
                    dist[nei]=dist[n]+1
                q.append(n)
        return dist

    def dijkstra(self,start):
        dist={node:float('inf') for node in graph}
        min_heap=heapq.heappush([(0,start)])
        visited=set()
        dist[start] = 0
        while min_heap:
            dist,node=heapq.heappop()
            if node in visited:
                continue
            visited.add(node)
            for nei,w in graph[node]:
                if dist[node]+w<dist[nei]:
                    dist[nei]=dist[node]+w
                    heapq.heappush(min_heap, (dist[nei], nei))

            return dist



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

g3 = graph(directed=True)
g3.add_edge(1, 2, 3)
g3.add_edge(1, 6, 4)
g3.add_edge(2, 3, 5)
g3.add_edge(2, 4, 6)
g3.add_edge(6, 7, 7)
g3.add_edge(6, 8, 8)
g3.add_edge(4, 5, 9)
g3.add_edge(7, 5, 10)

g3.display()
print("\nShortest Path in DAG from node 1:")
g3.shortest_path_in_DAG(1)


