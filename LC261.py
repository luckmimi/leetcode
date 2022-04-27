class UF:
    def __init__(self,n):
        self.count = n
        self.parent = [[] for i in range(n)]
        self.size = [[] for i in range(n)]
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
    def connected(self,p,q):
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
            
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for a, b in edges:
            if uf.connected(a,b):
                return False
            uf.union(a,b)
        return uf._count() == 1
