class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:    
        self.memo = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        return self.dfs(grid,0,0)
    def dfs(self,grid,i,j):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            if grid[i][j] == 1:
                return 0
            return 1
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 1:
            return 0
        if self.memo[i][j] > 0:
            return self.memo[i][j]
        down = self.dfs(grid, i + 1, j)
        right = self.dfs(grid,i, j + 1)
        res = down + right
        self.memo[i][j] = res
        return res
    
