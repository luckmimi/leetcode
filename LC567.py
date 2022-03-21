class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        need = collections.Counter(s2)
        window = collections.defaultdict()
        left, right, start,valid = 0, 0, 0, 0
        while right < len(s1):
            c = s1[right]
            right += 1
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1
                   
            
            while valid == len(need):
              
                if right - left == len(s2):
                    return True
                
                d = s1[left]
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return False
                    
                    
