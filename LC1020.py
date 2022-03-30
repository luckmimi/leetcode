class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid,x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0 
            d = [(1,0), (-1, 0), (0, -1), (0, 1)]
            res = 1
            for tx, ty in d:
                dfs(grid,x + tx, y + ty)
                res += 1
            return res
        for i in range(len(grid[0])):
            dfs(grid,0,i)
            dfs(grid,len(grid) - 1, i)
        for j in range(len(grid)):
            dfs(grid,j,0)
            dfs(grid,j,len(grid[0]) - 1)
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 1
        return res
                    
