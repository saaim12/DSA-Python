from collections import deque


def topo_sort_dfs(graph):
    n=len(graph)
    visited=set()
    recu_stack=set()
    order=[]

    def dfs(start_node):
        recu_stack.add(start_node)
        visited.add(start_node)

        for nei in graph[start_node]:
            if nei not in visited:
                if dfs(nei):
                    return True    #cycle detected
                elif nei in recu_stack:
                    return True   #cycle detected

        recu_stack.remove(start_node)
        order.append(start_node)
        return False # no cycle

    for i in range(n):
        if i not in visited:
            if dfs(i):
                return "Cycle is detected not a DAG"
    order.reverse()
    return order



def topo_sort_with_bfs_Khans_algorithm(graph):
    n= len(graph)
    indegree=[0]*n
    for i in range(n):
        for nei in graph[i]:
            indegree[nei]+=1

    q=deque()
    for i in range(len(indegree)):
        if indegree[i]==0:
            q.append(i)
    order=[]
    while q:
        node=q.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    if len(order) == n:
        return order
    else:
        return []  # cycle exists





graph = [
    [1, 2],  # 0 → 1,2
    [3],     # 1 → 3
    [3],     # 2 → 3
    []       # 3
]

print(topo_sort_dfs(graph))
print(topo_sort_with_bfs_Khans_algorithm(graph))