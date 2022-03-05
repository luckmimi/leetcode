class Solution:
    def minInsertions(self, s: str) -> int:

        cnt = 0 
        res = 0 
        i = 0
        while i < len(s):
            if s[i] == "(":
                cnt += 1
            else:
                if i + 1 < len(s) and s[i+1] == ")": 
                    cnt -= 1
                    i += 1
                else:
                    res += 1
                    cnt -= 1
            if cnt < 0 :
                    res += 1
                    cnt = 0
            i += 1     
            
        res += cnt * 2
        
        return res
                    
                    
