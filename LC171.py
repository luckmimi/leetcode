class Solution:
    def titleToNumber(self, cols: str) -> int:
        const = ord('A')
        res = 0 
        for c in cols:
            res = res* 26 + ord(c) - const + 1
        print(res)
        return res
