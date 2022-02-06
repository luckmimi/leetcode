from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.stack = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.stack) >= self.size:
            self.stack.popleft()
        self.stack.append(val)
        
        return sum(self.stack)/len(self.stack)
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
