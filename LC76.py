class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        print(len(need))
        valid = 0 
        window = collections.defaultdict()
        left = 0
        right = 0
        start = 0 
        res = math.inf
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                window[c] = window.get(c,0) + 1
                if need[c] == window[c]:
                    valid += 1
            while valid == len(need):
                
                if right - left < res:
                    res = right - left
                    start  = left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        
                        valid -= 1
                    window[d] -= 1
        
        if res == math.inf:
            return ''
        
        return s[start:start + res]
            
            
            
