from collections import defaultdict
import heapq
# N is number of vertex
# connection is array of edges with Value(weight)
# [source , destination , weight]
# eg : [0,1,3]
def minimumCost(N, connections):
    graph = defaultdict(list)
    start = connections[0][0]
	# Add all nodes because it's biderctional
    for src, dst, wt in connections:
        graph[src].append((dst, wt))
        graph[dst].append((src, wt))
     
    #Storing the data in parent Directory
    dist = {}
	# Using heap to find min wt
    heap = [(0, start)]
    while heap:
        ddist, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = ddist
        for neighbor, d in graph[node]:
            if neighbor not in dist:
                heapq.heappush (heap, (d, neighbor))
    return sum(dist.values()) if len(dist) == N else -1

if __name__ == '__main__':
    graph = [[0,1,2],
            [1,2,4],
            [2,3,5],
            [3,4,2],
            [2,4,2]]
    print(minimumCost(5,graph))