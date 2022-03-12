class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = set([0,1,8])
        s2 = set([2,5,6,9,1,8,0])
        def ok(x):
            cur = set([int(i) for i in str(x)])
            return cur.issubset(s2) and not cur.issubset(s1)
        count = 0
        for i in range(1,n+1):
            if ok(i):
                count += 1
        return count
            
