def Number_of_provinces(self, isConnected):
    # graph making
    graph = {i: [] for i in range(len(isConnected))}
    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if i != j and isConnected[i][j] == 1:
                graph[i].append(j)
    visited = set()

    def BFS(start):
        visited.add(start)
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

    provinces = 0
    for i in range(len(isConnected)):
        if i not in visited:
            BFS(i)
            provinces += 1

    return provinces


def Number_of_provinces_with_dfs(isConnected):
    graph = {i: [] for i in range(len(isConnected))}
    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if i != j and isConnected[i][j] == 1:
                graph[i].append(j)
    visited = set()

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
        return
    count=0
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            count+=1

    return count




