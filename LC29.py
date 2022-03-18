class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if  (dividend < 0) ^ (divisor < 0) else 1
        a = abs(dividend) 
        b = abs(divisor)
        
        res = 0
        while b<= a:
            mul = 1
            tmp = b
            while a >= (tmp <<1):
                tmp <<= 1
                mul <<= 1
            res += mul
            a -= tmp
        res *= sign
        if res > 2**31 -1 :
            return 2** 31 -1
        else:
            return res
