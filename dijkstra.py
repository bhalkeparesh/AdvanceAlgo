import heapq
import collections

def minimumCost(N,connections):
    weight = collections.defaultdict(dict)
    for u, v, w in connections:
        weight[u][v] = w
    heap = [(0, connections[0][0])]
    dist = {}
    while heap:
        time, u = heapq.heappop(heap)
        if u not in dist:
            dist[u] = time
            for v in weight[u]:
                heapq.heappush(heap, (dist[u] + weight[u][v], v))
    return max(dist.values()) if len(dist) == N else -1

if __name__ == '__main__':
    graph = [[0,1,2],
            [1,2,4],
            [2,3,5],
            [3,4,2],
            [2,4,2]]
    print(minimumCost(5,graph))


# Time: O(E+VlogV)
# Space: O(V+E)