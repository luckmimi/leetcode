from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, token in ((a,'a'),(b,'b'),(c,'c')):
            if count:
                heappush(max_heap,(-count,token))
        res = []
        while max_heap:
            first, char1 = heappop(max_heap)
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not max_heap: 
                    break
                second, char2 = heappop(max_heap)
                res.append(char2)
                second += 1
                if second < 0:
                    heappush(max_heap,(second,char2))
            res.append(char1)
            first += 1
            if first < 0:
                 heappush(max_heap,(first,char1))
        return ''.join(res)
                
            
