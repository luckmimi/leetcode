class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map = {'0':'0','1':'1','6':'9','9':'6','8':'8'}
        res = ''
        for d in num:
            if d in map:
                res += map[d]
            
        print(res)
        return res[::-1] == num
