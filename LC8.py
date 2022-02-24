class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or s == ' ':
            return 0 
        index = 0 
        while index < len(s) and s[index] == ' ':
            index += 1
        if index == len(s):
            return 0 
        res = 0 
        Neg = 1
        if s[index] == '+' or s[index] =='-':
            if s[index] == '-':
                Neg = -1
            index += 1
        if index == len(s): return 0
        while index <len(s):
            if s[index] <'0' or s[index] > '9':
                break
            res = res * 10 + int(s[index])
            index += 1
        return max(-2**31,min(res*Neg,2**31 - 1))
            
            
