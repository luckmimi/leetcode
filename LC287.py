class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] - 1 < n and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(n):
            if i + 1 != nums[i]:
                return nums[i]
        
        
      
