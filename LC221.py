class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
     
        for i in range(len(grid)):
            
                dp[i][0] =  int(grid[i][0])
        for j in range(len(grid[0])):
                dp[0][j] = int(grid[0][j])
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if grid[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        l = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l = max(l,dp[i][j])
        return l * l
