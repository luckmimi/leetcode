class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UF(n + 1)
        connections.sort(key = lambda x: x[2])
        print(connections)
        mst = 0
        for edge in connections:
            u = edge[0]
            v = edge[1]
            weight = edge[2]
            if uf.connected(u, v): 
                continue
            mst += weight
            uf.union(u, v)
        return mst if uf._count() == 2 else -1
class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [0] * n
        self.size = [0] * n
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = self.parent[rootP]
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = self.parent[rootQ]
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def _count(self):
        return self.count
        
