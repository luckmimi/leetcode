class NumArray:

    def __init__(self, nums: List[int]):
       self.presm = [0]*(len(nums) + 1)
       for i in range(len(nums)):
            self.presm[i] = self.presm[i - 1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.presm[right] - self.presm[left -1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
