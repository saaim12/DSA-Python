from collections import deque


class Solution:
    def minimumMultiplications(self, arr, start, end):
        MOD=10000
        dist=[float('inf')]* MOD

        q=deque([start])
        dist[start]=0
        while q:
            num =q.popleft()
            for val in arr:
               next=(num*val)%MOD
               if dist[next]>dist[num]+1:
                   dist[next]=dist[num]+1
                   q.append(next)

        return dist[end] if dist[end]!=float('inf') else -1











arr = [2, 5, 7]
start = 3
end = 30

S = Solution()
print(S.minimumMultiplications(arr, start, end))  # Output: 2
# 3*2=6, 6*5=30 (mod 10000)


