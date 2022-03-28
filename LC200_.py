class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 :
            return 0
        def dfs(grid,i,j):
            if i < 0 or j < 0 or j > len(grid[0]) - 1 or i > len(grid) - 1 or grid[i][j] == '0'  or (i,j) in visited:
                return
            d = [(0,1),(0,-1),(-1,0),(1,0)]
            grid[i][j] == '0'
            visited.add((i,j))
            for tx,ty in d:
                x = i + tx
                y = j + ty
                dfs(grid,x,y)
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res += 1
                    dfs(grid,i,j)

        return res
