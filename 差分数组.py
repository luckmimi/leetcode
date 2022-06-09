class DF:
    def __init__(self, nums):
        assert len(nums) > 0
        self.diff = [0]*len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    def results(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = self.diff[i] + res[i-1]
        return res
