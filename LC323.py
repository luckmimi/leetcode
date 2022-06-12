class UF:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [0 for _ in range(n)]
        self.count = n
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = rootY
        self.size[rootY] += self.size[rootX]
        self.count -= 1
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def _count(self):
        return self.count 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        return uf._count()
        
