class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1]*n for i in range(m)]
        
        for col in range(1,m):
            for row in range(1,n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
        
        return d[m - 1][n - 1]
        
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m-1,n) + self.uniquePaths(m,n - 1)
#         visited = set()
#         self.ans = set()
#         def dfs(x,y,m,n,cur):
#             if x == m - 1 and y == n - 1:
#                 self.ans.add(cur)
#                 return
#             if x >= m or y >= n :
#                 return
#             visited.add((x,y))
           
#             dfs(x + 1, y, m, n, cur + 'Right')
#             dfs(x, y + 1, m, n, cur + 'Down')
        
#         dfs(0,0,m,n,'')
#         return len(self.ans)
