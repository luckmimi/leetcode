class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = set()
        def dfs(grid,x, y, pos,cur):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 
            grid[x][y] = 0 
            self.pos += str(cur) + ','
            d = [(-1,0),(1,0),(0,-1),(0,1)]
            for i, (tx,ty) in enumerate(d):
                dfs(grid, tx + x,ty + y,pos, i)
            self.pos  += str(-cur) + ','
           
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.pos = ''
                    dfs(grid,i,j,pos,666)
                    res.add(self.pos)
                    
                 
        return len(res)
