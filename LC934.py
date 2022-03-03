class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        def dfs(grid,x,y,q):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                return 
            
            grid[x][y] = 2
            q.put((x,y))
            dfs(grid, x - 1, y,q )
            dfs(grid,x + 1, y,q)
            dfs(grid,x,y - 1,q)
            dfs(grid,x, y + 1,q)
        from queue import Queue
        q = Queue()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if not found and grid[i][j] == 1:
                    dfs(grid,i,j,q)
                    found = True
        steps = 0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while not q.empty():
            
            n = q.qsize()
            for _ in range(n):
                i,j = q.get()
                for (tx, ty) in directions:
                    x = i + tx
                    y = j + ty
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 2:
                        continue
                    if grid[x][y] == 1:
                        return steps
                    grid[x][y] = 2
                    q.put((x,y))
                
            steps += 1
        return -1
            
                    
