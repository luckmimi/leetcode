class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        distance= {(0,0,k):0}
        
        q = collections.deque([])
        q.append((0,0,k))
        while q:
            x,y, cur_k = q.popleft()
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return distance[(x,y, cur_k)]
            for dx,dy in ((0, 1),(0, -1),(-1, 0), (1, 0)):
                new_x, new_y = dx + x, dy + y
                
                if not self.is_valid(grid,new_x,new_y,distance,cur_k):
                    continue
                if grid[new_x][new_y] == 1 and cur_k > 0 and (new_x, new_y,cur_k - 1) not in distance:
                    q.append((new_x,new_y,cur_k - 1))
                    distance[(new_x, new_y,cur_k - 1)] = distance[(x,y,cur_k)] + 1
           
                elif  grid[new_x][new_y] == 0:
                    q.append((new_x,new_y,cur_k))
                    distance[(new_x,new_y,cur_k)]=  distance[(x,y,cur_k)] + 1

        return -1
                    
    def is_valid(self,grid,x,y,distance,cur_k):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x,y,cur_k) in distance:
            return False
        return True
