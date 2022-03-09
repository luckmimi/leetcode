class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        def dfs(cur,parent):
            if cur in visited:return True
            visited.add(cur)
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            i,j = cur
            childs = []
            for tx,ty in dirs:
                x = i + tx
                y = j + ty
                if 0<= x < len(grid) and 0 <=y < len(grid[0]) and grid[x][y] == grid[i][j] and (x,y)!= parent:
                    childs.append((x,y))

            for child in childs:
                if dfs(child,cur):
                    return True

        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if (i,j) not in visited:
                        if dfs((i,j),None): return True

        return False
   
  
                    
