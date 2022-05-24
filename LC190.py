class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0: return n
        res = 0 
        for i in range(32):
            res <<= 1
            if n & 1 == 1: res += 1
            n >>= 1
        return res
