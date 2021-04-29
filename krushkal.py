# The time complexity for union and find methods for DisjointSet are as follows:

# Without any optimization - O(N)
# With union by rank - O(log N)
# With union by rank and path compression - O(N)
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
    
    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    


def minimumCost(N, connections):
    
    # sort based on cost (i.e. distance)
    connections.sort(key=lambda x : x[2])
    
    # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
    res = 0
    ds = DisjointSet(N)
    for u,v,cost in connections:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            res += cost
    
    return res

if __name__ == '__main__':
    graph = [[0,1,2],
            [1,2,4],
            [2,3,5],
            [3,4,2],
            [2,4,2]]
    print(minimumCost(5,graph))