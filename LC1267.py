class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0 
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans = self.dfs(grid,i,j,visited)
                    if ans  > 1:
                        res += ans
        return res 
    def dfs(self,grid,x,y,visited):
        ans = 0 
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x,y) in visited:
            return 0
        visited.add((x,y))
        ans += 1
        for new_x in range(len(grid)):
                ans += self.dfs(grid,new_x,y,visited)
        for new_y in range(len(grid[0])):
        
                ans += self.dfs(grid,x,new_y,visited)
        return ans
