class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        maxL = 0
        start = 0 
        for i in range(len(s)):
            missing = 0 
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                
                    if (s[j].lower() not in seen) or (s[j].upper() not in seen):
                        missing += 1
                    else:
                        missing -= 1
                if missing == 0 and (j - i + 1 ) > maxL:
                    maxL = j -  i + 1
                    start = i 
        return s[start: start + maxL]
