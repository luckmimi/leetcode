class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        leftsum = 0 
        for i, x in enumerate(nums):
            if leftsum == (sm - leftsum - x):
                return i
            leftsum += x
        return -1
