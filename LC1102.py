class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        left = 0 
        right = min(grid[0][0],grid[-1][-1])
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.valid(mid,grid):
                left = mid
            else:
                right = mid - 1
        if self.valid(right,grid):
            return right
        return left
    def valid(self,val,grid):
        memo = [[0]*len(grid[0]) for _ in range(len(grid))]
        def dfs(x,y,grid,val):
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return True
            memo[x][y] = 1
            d = [(1,0),(0,1),(-1,0),(0,-1)]
            for tx,ty in d:
                x1 = tx + x
                y1 = ty + y
                if x1 >= 0 and y1 >= 0 and x1 <= len(grid) - 1 and y1 <= len(grid[0]) - 1 and not memo[x1][y1] and   val <= grid[x1][y1] and dfs(x1,y1,grid,val):
                    return True
            return False
        return dfs(0,0,grid,val)
    
    

    

# backtracking
# class Solution:
#     def maximumMinimumPath(self, grid: List[List[int]]) -> int:
#         m = len(grid) - 1
#         n = len(grid[0]) - 1
#         self.res = float('-inf')
#         seen = [[False]*len(grid[0]) for _ in range(len(grid))]
#         seen[0][0] = True
#         cur = [grid[0][0]]
#         self.dfs(grid,0,0,cur,seen)
#         return self.res
    
#     def dfs(self,grid, x,y,cur,seen):
   
#             if x == len(grid) - 1 and y == len(grid[0]) - 1:
#                 print(cur)
#                 self.res = max(self.res, min(cur[:]))
#                 return
   
#             d = [(1,0),(0,1),(-1,0),(0,-1)]
#             for tx,ty in d:
#                 x1 = tx + x
#                 y1 = ty + y
                
#                 if x1< 0 or y1 < 0  or  x1 > len(grid) - 1 or y1 > len(grid[0]) - 1 or seen[x1][y1]:
#                     continue
#                 seen[x1][y1] = True
#                 # cur.append(grid[x1][y1])
#                 self.dfs(grid,x1,y1, cur + [grid[x1][y1]] ,seen)
#                 # cur.pop() 
#                 seen[x1][y1] = False
     
