class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = {}
        last = n - 1
        self.size = n - len(blacklist)
        for b in blacklist:
            self.map[b] = 666
        for b in blacklist:
            if b >= self.size: continue
            while last in self.map:
                last -= 1
            self.map[b] = last
            last -= 1
            
    def pick(self) -> int:
        p = random.randint(0,self.size -1)
        if p in self.map:
            return self.map[p]
        return p
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
