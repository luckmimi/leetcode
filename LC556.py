class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        i = len(s) - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
        if i < 0 :
            return -1
        left = i + 1
        right = len(s) - 1
        while right > left and s[right] <= s[i]:
                right -= 1
        s[right],s[i] = s[i],s[right]
        s[i+ 1:] = s[i+1:][::-1]
        
        res = ''.join(s)
        
        return res if int(res) <= 2**31-1 else -1
                
