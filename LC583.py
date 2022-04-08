class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0]*(len(w2)+1) for _ in range(len(w1)+1)]
        for i in range(1,len(w1)+1):
            for j in range(1,len(w2)+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return len(w1)  -2* dp[len(w1)][len(w2)] +len(w2)
        
