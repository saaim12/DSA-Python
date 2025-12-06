import heapq
from collections import deque, defaultdict
from operator import truediv


def print_matrix(mat):
    print("\nEfforts matrix:")
    for row in mat:
        print(" ".join(f"{x:4}" if x != float('inf') else " inf" for x in row))
    print()


def minimumEffortPath(heights):
    rows = len(heights)
    cols = len(heights[0])

    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_heap = [(0, 0, 0)]  # diff, row, col

    print_matrix(efforts)

    while min_heap:
        curr_diff, row, col = heapq.heappop(min_heap)

        # ⭐ WHEN WE POP DESTINATION → BEST POSSIBLE
        if row == rows - 1 and col == cols - 1:
            print("Reached destination with effort:", curr_diff)
            return curr_diff

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                diff = abs(heights[nr][nc] - heights[row][col])
                new_diff = max(curr_diff, diff)

                if new_diff < efforts[nr][nc]:
                    efforts[nr][nc] = new_diff
                    heapq.heappush(min_heap, (new_diff, nr, nc))

                    print_matrix(efforts)

    return efforts[rows - 1][cols - 1]


print(minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))


def shortestPathBinaryMatrix(grid):
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
        return -1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    q = deque([(1, 0, 0)])  # dist , row ,col
    vis = set([(0, 0)])
    while q:
        dist, row, col = q.popleft()
        if row == rows - 1 and col == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = dr + row, dc + col
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in vis and grid[nr][nc] == 0:
                q.append((dist + 1, nr, nc))
                vis.add((nr, nc))

    return -1
print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))




def eventualSafeNodes(arr):
    graph = {i: [] for i in range(len(arr))}
    for i, arr in enumerate(arr):
        for element in arr:
            graph[i].append(element)
    #now dfs for cycle detection
    visited=set()
    path=set()
    def dfs(node):
        visited.add(node)
        path.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                   return True
            elif nei in path:
                return True
        path.remove(node)

        return False


    res=[]
    for i in range(len(graph)):
        if not dfs(i):
            res.append(i)

    return res

print(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(eventualSafeNodes([[1],[2],[3],[1]]))


def findEventualSafeNodes__optimized(graph_edges):
    """
    Finds all nodes in a directed graph that are eventually safe.
    A node is eventually safe if every path starting from it leads
    to a terminal node (a node with no outgoing edges) and does not
    get stuck in a cycle.

    :type graph_edges: List[List[int]]  # adjacency list representation
    :rtype: List[int]  # sorted list of safe nodes
    """
    ## this is with memeorization
    n = len(graph_edges)
    # Build a graph dictionary from the adjacency list
    graph = {i: graph_edges[i] for i in range(n)}

    # Memoization dictionary: safe[node] = True if node is eventually safe
    safe = {}

    def dfs(node, path):
        """
        Depth-First Search to check if a node is eventually safe.
        Uses path set to detect cycles and memoization to reuse results.

        :param node: current node
        :param path: set of nodes in current DFS path (for cycle detection)
        :return: True if node is eventually safe, False otherwise
        """

        # If already computed, return the stored result
        if node in safe:
            return safe[node]

        # If current node is in the path, a cycle is detected → unsafe
        if node in path:
            safe[node] = False
            return False

        # Add current node to the DFS path
        path.add(node)

        # Explore all neighbors
        for neighbor in graph[node]:
            # If any neighbor is unsafe, current node is unsafe
            if not dfs(neighbor, path):
                safe[node] = False
                path.remove(node)
                return False

        # Remove node from current path after exploration
        path.remove(node)

        # All neighbors are safe → current node is safe
        safe[node] = True
        return True

    # Collect all nodes that are eventually safe
    result = []
    for node in range(n):
        if dfs(node, set()):
            result.append(node)

    # Return nodes in sorted order
    return sorted(result)
print(findEventualSafeNodes__optimized([[1, 2], [2, 3], [5], [0], [5], [], []]))


def minCost(maxTime, edges, passingFees):
    n = len(passingFees)
    adj = [[] for _ in range(n)]
    for edge in edges:
        u, v, t = edge
        adj[u].append((v, t, passingFees[v]))
        adj[v].append((u, t, passingFees[u]))
    minTime = [float('inf') for _ in range(n)]
    pq = []
    heapq.heappush(pq, (passingFees[0], 0, 0)) # cost, time, node
    while pq:
        cost, time, node = heapq.heappop(pq)
        if time > maxTime or time >= minTime[node]:
            continue
        if node == n - 1:
            return cost
        minTime[node] = time
        for v, t, c in adj[node]:
            if time + t <= maxTime:
                heapq.heappush(pq, (cost + c, time + t, v))

    return -1



### this is better solution from lc
# import heapq
# from collections import defaultdict
#
#
# class Solution(object):
#     def minCost(self, maxTime, edges, passingFees):
#         """
#         :type maxTime: int
#         :type edges: List[List[int]]
#         :type passingFees: List[int]
#         :rtype: int
#         """
#         n = len(passingFees)
#
#         # Build adjacency list
#         graph = defaultdict(list)
#         for u, v, t in edges:
#             graph[u].append((v, t))
#             graph[v].append((u, t))
#
#         # Priority queue: (total_cost, total_time, node)
#         pq = [(passingFees[0], 0, 0)]  # start at city 0
#         heapq.heapify(pq)
#
#         # best_time[i] = minimum time we have reached node i
#         best_time = [float('inf')] * n
#         best_time[0] = 0
#
#         while pq:
#             cost, time, node = heapq.heappop(pq)
#
#             # If reached destination within time
#             if node == n - 1:
#                 return cost
#
#             # Explore neighbors
#             for nei, t in graph[node]:
#                 new_time = time + t
#                 new_cost = cost + passingFees[nei]
#
#                 # Only proceed if within maxTime
#                 if new_time <= maxTime:
#                     # Prune paths that are slower and not cheaper
#                     if new_time < best_time[nei]:
#                         best_time[nei] = new_time
#                         heapq.heappush(pq, (new_cost, new_time, nei))
#
#         # If not reachable
#         return -1
print(minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))
print(minCost(maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))
print(minCost(maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))

