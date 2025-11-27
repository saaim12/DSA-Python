def floyd_warshall(n, edges):
    """
    n: number of vertices (0 to n-1)
    edges: list of [u, v, w] representing edge u->v with weight w
    """
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0

    # Fill in initial edges
    for u, v, w in edges:
        dist[u][v] = w  # for directed graph
        # dist[v][u] = w  # uncomment if undirected graph

    # Main Floyd-Warshall loops
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n = 4
edges = [
    [0, 1, 5],
    [0, 3, 10],
    [1, 2, 3],
    [2, 3, 1]
]

dist = floyd_warshall(n, edges)
for row in dist:
    print(row)
