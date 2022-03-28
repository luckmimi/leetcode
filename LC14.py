class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        res = ''
        m = min([len(i) for i in s])
        for i in range(m):
            cur = s[0][i]
            for j in range(1,len(s)):
                if cur not in s[j][i]:
                    return res
            res += cur
        print(res)
        return res
        
