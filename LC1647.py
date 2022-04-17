class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0 
        char_counts = collections.Counter(s)
        seen = set()
        for char, count in char_counts.items():
            while count > 0 and count in seen:
                count -= 1
                res += 1
            seen.add(count)
        return res
   
            
            
