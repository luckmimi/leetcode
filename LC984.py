class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        stack = []
        heapq.heappush(stack,(-a,'a'))
        heapq.heappush(stack,(-b,'b'))
        res = ''
        
        while stack:
            cnt, char = heapq.heappop(stack)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                cnt2, char2 = heapq.heappop(stack)
                res += char2
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(stack,(cnt2,char2))
                
            else:
                res += char
                cnt += 1
            if cnt < 0 :
                    heapq.heappush(stack,(cnt,char))
        # print(res)
        return res
                    
