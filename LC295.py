from heapq import heappush,heappop
class MedianFinder:
    
    def __init__(self):
        self.small = []
        self.big  = []
      
        

    def addNum(self, num: int) -> None:
        
        if len(self.big) > len(self.small):
            heappush(self.big,num)
            cur = heappop(self.big)
            heappush(self.small, -cur)
        else:
            heappush(self.small,-num)
            cur = heappop(self.small)
            heappush(self.big, -cur)
                

    def findMedian(self) -> float:
        if  len(self.big) == len(self.small):
            return (-self.small[0] + self.big[0])/2
        return self.big[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
