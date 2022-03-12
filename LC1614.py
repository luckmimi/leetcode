class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        i = 0 
        for c in s:
            
            if c == '(':
                i += 1
                count = max(count,i)
                
            elif c == ')':
                i -= 1
            
        return count
