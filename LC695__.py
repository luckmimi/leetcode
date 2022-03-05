class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = self.dfs(grid,i,j)
                    self.res = max(self.res, res)
        return self.res
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] !=1:
            return 0
        grid[i][j] = 2
        res = 1
        for tx,ty in ((0,1),(0,-1),(1,0),(-1,0)):
            x = tx + i
            y = ty + j
            res += self.dfs(grid,x, y)
        return res
        
