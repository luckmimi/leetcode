class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {v:k for k,v in enumerate(order)}
        
        res = ['']*len(map.keys())
        left = ''
        for c in s:
            if c in map:
                res[map[c]] += c
            else:
                left += c
    
        return ''.join(res) + left
