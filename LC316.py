class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ ={}
        visited = set()
        res = []
        for i, c in enumerate(s):
            last_occ[c] = i
        for i, c in enumerate(s):
            if c not in visited:
                while res and last_occ[res[-1]] > i and res[-1] > c:
                    
                    visited.remove(res.pop())
                visited.add(c)
                res.append(c)
        
        return ''.join(res)
