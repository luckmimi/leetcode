class UF:
    def __init__(self, n):
        self.parent = [ i for i in range(n)]
        self.size = [1] * n
        self.count = n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y ):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = rootY
        self.size[rootY] += self.size[rootX]
        self.count -= 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    def _count(self):
        return self.count
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i,j, abs(x1 - x2) + abs(y1 - y2)))
        edges.sort(key = lambda x: x[2])
        mst = 0 
        for edge in edges:
            a, b, cost = edge
            if uf.is_connected(a,b):
                continue
            uf.union(a,b)
            mst += cost
        
        return mst
        
            
        

                
