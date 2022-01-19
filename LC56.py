class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        merged = [intervals[0]]
        for interval in intervals[1:]:
            a,b = merged[-1]
            c, d = interval
            if b >= c:
                merged[-1] = [a,max(b,d)]
            else:
                merged.append(interval)
        return merged
        
