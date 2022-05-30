class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        line = []
       
        for st, end in intervals:
            line.append((st,1))
            line.append((end,-1))
        line.sort()
        res = 0
        cur = 0 
        for a, delta in line:
            cur += delta
            res = max(cur, res)
        return res
