    def shortestDistance(self, grid: List[List[int]]) -> int: # 枚举house，然后看house到每个空地的距离，求最小
        house = 0  
        if not grid or not grid[0]: return 0 
        
        distance_sum = collections.defaultdict()
        reachable_count = collections.defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house += 1
                    self.bfs(grid,i,j,distance_sum, reachable_count)
        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in reachable_count or reachable_count[(i,j)] != house:
                    continue
                res = min(res, distance_sum[(i,j)])
        return res if res != float('inf') else -1
    def bfs(self,grid,i,j,distance_sum, reachable_count):
        distance = {(i,j):0}
        q = collections.deque([(i,j)])
        while q:
            x, y = q.popleft()
            for (dx,dy) in ((0,1),(0,-1),(1,0),(-1,0)):
                new_x, new_y = x + dx, y + dy 
                if not self.is_valid(grid, new_x, new_y) or (new_x, new_y) in distance:
                    continue
                distance[(new_x,new_y)] = distance[(x,y)] + 1
                q.append((new_x, new_y))
                if (new_x, new_y) not in reachable_count:
                        distance_sum[(new_x, new_y)] = 0 
                        reachable_count[(new_x, new_y)] = 0 
                distance_sum[(new_x, new_y)] += distance[(new_x, new_y)]
                reachable_count[(new_x, new_y)] += 1
    
  
    def is_valid(self,grid,x,y):
        if x < 0 or x  > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            return False
        return grid[x][y] == 0
