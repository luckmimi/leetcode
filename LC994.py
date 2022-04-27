class OrangeType:
    EMPTY = 0 
    FRESH = 1
    ROTTEN = 2
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque([])
        fresh_count = 0 
        time_spend = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1
        while q and fresh_count > 0:
            
            for i in range(len(q)):
                x, y  = q.popleft()
                for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0  or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] != 1:
                        continue
                    grid[new_x][new_y] = 2
                    fresh_count -= 1
                    q.append((new_x,new_y))
            time_spend += 1
        return time_spend if fresh_count == 0 else -1
                        
                
