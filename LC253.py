class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort()
        heap = [intervals[0][1]]
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start >= heap[0]:
                heapq.heapreplace(heap,end)
            else:
                heapq.heappush(heap,end)
            print(heap)
               
        return len(heap)
            
