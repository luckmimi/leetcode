class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid2,x,y):
            if x < 0 or y < 0 or x >= len(grid2) or y >= len(grid2[0]) or grid2[x][y] == 0:
                return 
            grid2[x][y] = 0 
            for tx,ty in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(grid2,x + tx, y + ty)
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] != grid2[i][j] and grid2[i][j] == 1:
                    dfs(grid2,i,j)
        res = 0 
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    res += 1
                    dfs(grid2,i,j)
        return res
            
