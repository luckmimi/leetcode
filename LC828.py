class Solution:
    def uniqueLetterString(self, s: str) -> int:
        lastPos = [[-1,-1] ] * 26
        res = 0 
        for i in range(len(s)):
            tmp = ord(s[i]) - ord('A')
            # print(tmp)
            j, k = lastPos[tmp]
            res += (i - j) * (j - k)
            lastPos[tmp] = [i, j]
        for i,j in lastPos:
            
            res += (i - j) * (len(s) - i)
        return res
