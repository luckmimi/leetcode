class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = collections.Counter(s)
        f = set([k for k,v in m.items() if v == 1])
        for i, k in enumerate(s):
            if k in f:
                return i
        return -1 
