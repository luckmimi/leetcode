class Solution:

    def __init__(self, nums: List[int]):
        from collections import defaultdict
        self.nums = defaultdict(list)
        for index, n in enumerate(nums):
            self.nums[n] = self.nums.get(n,[])+[index]
            
        

    def pick(self, target: int) -> int:
        import random
        res = self.nums[target]
        res.sort()
        print(res)
        return random.choice(res)
        
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
