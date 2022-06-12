class UF:
    def __init__(self,n):
        self.parent = [ i for i in range(n)]
        self.size = [1] * n
        self.count = n
    # def add(self,val):
    #     if val in self.parent:
    #         return
    #     self.parent[val] = None
    #     self.size[val] += 1
    #     self.count += 1
    def union(self,x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = self.parent[rootY]
        self.size[rootY] += self.size[rootX]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def connected(self,x, y):
        return self.find(x) == self.find(y)
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return 
        m = len(board)
        n = len(board[0])
        uf = UF(m * n + 1)
        dummy = m * n 
        for i in range(m):
            if board[i][0] == '0':
                uf.union(dummy, i * n)
            if board[i][n-1] == '0':
                uf.union(dummy, i * n + n - 1)
        for j in range(n):
            if board[0][j] == '0':
                uf.union(dummy, j)
            if board[m - 1][j] == '0':
                uf.union(dummy, (m - 1) * n + j)
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == '0':
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if board[x][y] == '0':
                            uf.union(x * n + y , i * n + j)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                
                if not uf.connected(dummy, i * n + j):
                    
                    board[i][j] = 'X'
        return board
