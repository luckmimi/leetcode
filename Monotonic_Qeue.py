class MonotonicQueue:
    def __init__(self):
        self.q = deque([])
        self.max_q= deque([]) # decreasing montonic, max in the front 
        self.min_q = deque([]) # increading montonic, min in the front 
    def push(self, val):
        self.q.append(val)
        while self.max_q and self.max_q[-1] < val:
            self.max_q.pop()
        self.max_q.append(val)
        while self.min_q and self.min_q[-1] > val:
            self.min_q.pop()
        self.min_q.append(val)
    def pop(self):
        del_val = self.q.popleft()
        if del_val == self.max_q[0]:
            self.max_q.popleft()
        if del_val == self.min_q[0]:
            self.min_q.popleft()
        return del_val
    def max(self):
        return self.max_q[0]
    def min(self):
        return self.min_q[0]
    def size(self):
        return len(self.q)
    def isEmpty(self):
        return len(self.q) == 0
