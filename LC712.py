class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        self.memo =[[-1]*(n) for _ in range(m)]
        return self.dp(s1,0,s2,0)
    def dp(self,s1,i,s2,j):
        res = 0
        if i == len(s1):
            for k in range(j,len(s2)):
                res += ord(s2[k])
            return res
        if j == len(s2):
            for k in range(i,len(s1)):
                res += ord(s1[k])
            return res
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1,i+1, s2,j+1)
        else:
            self.memo[i][j] = min(ord(s2[j]) + self.dp(s1,i,s2,j+1),ord(s1[i])+ self.dp(s1,i+1,s2,j))
            
    
        return self.memo[i][j]
        
