class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_f = [0] * len(s)
        b_f[0] = (s[0] == 'b')
        for i in range(1,len(s)):
            b_f[i] = b_f[i-1] + (s[i] == 'b')
        res = math.inf
        a_b = 0 
        for i in range(len(s) - 1, -1, -1):
            a_b += (s[i] == 'a')
            res = min(res, b_f[i] + a_b - 1)
        return res
