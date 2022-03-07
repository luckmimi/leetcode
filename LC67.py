class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a =='' or b == '':
            return b or a
        p = len(a) - 1
        q = len(b) - 1
        res = ''
        carry = 0
        while  p >=0 or q >= 0:
            if p >= 0:
                a1 = int(a[p])
            else:
                a1 = 0 
            if q >= 0:
                b1 = int(b[q])
            else:
                b1 = 0
            p -= 1
            q -= 1
            sm = a1 + b1 + carry
            res = str(sm % 2) + res
            carry = sm // 2
        if carry:
            res =  str(carry) + res
        return res 
        
