class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]== 1:
            return -1 
        from collections import deque
        dirs = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited = {(0,0)}
        q = deque([(0,0,1)])
        while q:
            curx,cury, curd = q.popleft()
            if curx == cury == n - 1:
                return curd
            for dx,dy in dirs:
                tx, ty = curx + dx, cury + dy
            
                if (tx,ty) not in visited and tx >=0 and tx < n and ty>=0 and ty< n and grid[tx][ty] == 0:
                    q.append((tx,ty,curd+1))
                    
                    visited.add((tx,ty))
        return -1
                    
            
            
            
