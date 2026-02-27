from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])
    res = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        res.append(level)

    return res

def DFS(start,visited,res):
    if visited is None:
        visited=set()
    if res is None:
        res=[]

    visited.add(start)
    res.append(start)
    for nei in graph[start]:
        if nei not in visited:
            DFS(nei,visited,res)

    return res

 
# ----- Graph Definition (Adjacency List) -----
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# ----- Run BFS -----
start_node = 0
result = bfs(graph, start_node)
result=DFS(start_node,set(),[])
print("Level Order BFS:", result)