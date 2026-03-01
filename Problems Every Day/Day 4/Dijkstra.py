import heapq


def dijkstra_s(graph,start_node):
    distances={i:float('inf') for i in range(len(graph))}
    distances[start_node]=0
    pq=([(0,start_node)])

    while pq:
        dist,node=heapq.heappop(pq)
        if dist>distances[node]:
            continue
        for nei,w in graph[node]:
            new_dist=dist+w
            if new_dist<distances[nei]:
                distances[nei]=new_dist
                heapq.heappush(pq,(new_dist,nei))


    return distances








graph_dict = {
    0: [(1,5), (2,3)],
    1: [(3,6), (4,2)],
    2: [(3,7), (4,4)],
    3: [(5,1)],
    4: [(5,2), (6,3)],
    5: [],
    6: [(3,1)]
}


# 0 --5--> 1 --6--> 3 --1--> 5
#  \        \
#   3        2
#    \        \
#     --> 2 --7--> 3
#          \
#           4 --2--> 5
#            \
#             6 --1--> 3

print(dijkstra_s(graph_dict,0))