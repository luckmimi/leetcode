class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backtrack(s):
            ans = 0 
            if s:
                for i in range(1,len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        ans = max(ans, 1 + backtrack(s[i:]))
                        seen.remove(candidate)
            return ans
                        
                
        
        return backtrack(s)
        
            
