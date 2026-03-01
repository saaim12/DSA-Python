from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = {i: [] for i in range(n)}
        q = deque([])
        for tup in flights:
            u, v, w = tup
            graph[u].append((v, w))

        q.append((0, src, 0))  # dist,node , stops
        dist = [float('inf')] * n
        dist[src]=0
        while q:
            dists,node,stops=q.popleft()
            if stops>k:
                continue

            for nei,w in graph[node]:
                new_dist=dists+w
                if dist[nei]>new_dist:
                    q.append((new_dist,nei,stops+1))
                    dist[nei]=new_dist


        return dist[dst] if dist[dst] !=float('inf') else -1



flights = [[0,1,100],[1,2,100],[0,2,500]]
S = Solution()
print(S.findCheapestPrice(3, flights, 0, 2, 1))  # Output: 200