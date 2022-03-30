class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            res = []
            for c in s:
                if c == '#':
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return ''.join(res)
        return helper(s) == helper(t)
