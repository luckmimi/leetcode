class Type:
    EMPTY = 0 
    BUILDING = 1
    OBSTACLE = 2
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int: # 枚举房子，到每个空地的距离， 优化
       
        if not grid or not grid[0]: return 0 
        count = 0 
        total_sum = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_dist = self.bfs(grid,i,j,count,total_sum)
                    count += 1
                    if min_dist == float('inf'):
                        return -1
        return min_dist
    def bfs(self,grid,i,j,curr_count, total_sum):
        min_distance = float('inf')
        q = collections.deque([(i,j,0)])
        while q:
            x, y, curr_step = q.popleft()
            for (dx,dy) in ((0,1),(0,-1),(1,0),(-1,0)):
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(grid, new_x, new_y,curr_count) :
                        continue
                total_sum[new_x][new_y] += curr_step + 1
                min_distance = min(min_distance, total_sum[new_x][new_y])
                
                grid[new_x][new_y] -= 1
                q.append((new_x, new_y,curr_step + 1))
        return min_distance
  
    def is_valid(self,grid,x,y,curr_count):
        if x < 0 or x  > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            return False
        return grid[x][y] == -curr_count
    
                    
