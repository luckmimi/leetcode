class Solution:
    def checkRecord(self, n: int) -> int:
        # dp[i][j][k]: i: record, j: L 0,1,2, k : A 0;1
        MOD = 10 ** 9 + 7
        dp = [[[0 for i in range(2)] for j in range(3)] for k in range(2)]
        dp[1][0][0] = 1
        dp[1][1][0] = 1
        dp[1][0][1] = 1
        dp[1][1][1] = 0 
        dp[1][2][0] = 0
        dp[1][2][1] = 0
        for i in range(2,n + 1):
            dp[i%2][0][0] = (dp[(i-1)%2][0][0] + dp[(i-1)%2][1][0] + dp[(i-1)%2][2][0]) % MOD
            dp[i%2][1][0] = dp[(i-1)%2][0][0] % MOD
            dp[i%2][0][1] = (dp[(i-1)%2][0][0] + dp[(i-1)%2][1][0] + dp[(i-1)%2][2][0]) % MOD + (dp[(i-1)%2][0][1] + dp[(i-1)%2][1][1] + dp[(i-1)%2][2][1]) % MOD
            dp[i%2][1][1] = dp[(i-1)%2][0][1] % MOD 
            dp[i%2][2][0] = dp[(i-1)%2][1][0] % MOD
            dp[i%2][2][1] = dp[(i-1)%2][1][1] % MOD
        totSum = 0 
        for i in range(3):
            for j in range(2):
                totSum += dp[(n)%2][i][j]
                totSum %= MOD
        return totSum
                                                      
                                                    
                                                
                                                      
    # recursive
    # def checkRecord(self, n: int) -> int:
    #     MOD = 10 ** 9 + 7
    #     memo = {}
    #     def dfs(n,consecutive, hasA):
    #         if n == 0:
    #             return 1
    #         if (n, consecutive,hasA) in memo:
    #             return memo[(n,consecutive, hasA)]
    #         tmp = 0 
    #         if not hasA:
    #             tmp += dfs(n - 1, 0, True)
    #             tmp %= MOD
    #         if consecutive < 2:
    #             tmp += dfs(n - 1, consecutive + 1, hasA)
    #             tmp %= MOD
    #         tmp += dfs(n-1, 0, hasA)
    #         tmp %= MOD
    #         memo[(n,consecutive, hasA)] = tmp
    #         return tmp
    #     return dfs(n,0,False)
