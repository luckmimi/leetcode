class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[money] 组成amount 的coin combination 
    # dp[i][j] 定义：若只使用前i个物品 可以重复使用，当背包容量为j时，有dp【i】【j]中方案
    
        dp = [[0] * (amount+1)  for _ in range (len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in  range(1,len(coins) + 1):
            for j in range(1,amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    
                    dp[i][j] +=  dp[i][j - coins[i - 1]]
       
        return dp[len(coins)][amount]
