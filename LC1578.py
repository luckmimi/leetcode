class Solution:
    def minCost(self, s: str, time: List[int]) -> int:
        res = max_cost = 0 
        for i in range(len(s)):
            if i > 0 and s[i - 1] != s[i]:
                max_cost = 0
            res += min(max_cost, time[i])
            max_cost = max(max_cost, time[i])
        return res 
