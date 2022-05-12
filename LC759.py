"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        import heapq
        h = []
        for interval in schedule:
            for inter in interval:
                heapq.heappush(h,(inter.start,-1))
                heapq.heappush(h,(inter.end, 1))
      
        n = len(h)
        cnt = 0 
        res = []
        while n > 1:
            left = heapq.heappop(h)
            right = h[0]
        
            cnt += left[1]
            if left[1] == 1 and right[1] == -1 and cnt == 0:
                
                res.append(Interval(left[0],right[0]))
            n -= 1
        return res
