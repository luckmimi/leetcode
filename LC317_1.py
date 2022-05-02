class Type:
    EMPTY = 0 
    BUILDING = 1
    OBSTACLE = 2
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0    
    
        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 :
                    distance = self.dfs(grid,i,j)
                    distance_sum = self.distance_sum(grid,distance)
                    res = min(res, distance_sum)
        return res if res != float('inf') else -1 
            
    def dfs(self,grid, i, j):
        distance = {(i,j):0}
        q = collections.deque([(i,j)])
        while q:
            x, y = q.popleft()
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                new_x, new_y = x + dx, y + dy 
                if not self.is_valid(grid, new_x, new_y) or (new_x, new_y)  in distance:
                    continue
                distance[(new_x,new_y)] = distance[(x,y)] + 1
                if grid[new_x][new_y] == 0:
                        q.append((new_x,new_y))
        return distance
    def distance_sum(self,grid,distance):
        sm = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i,j) not in distance:
                         return float('inf')
                    sm += distance[(i,j)]
           
        return sm
    def is_valid(self,grid,x,y):
        if x < 0 or x  > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            return False
        return grid[x][y] != 2
    
                    
