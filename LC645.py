class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] - 1 < n and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
                
        for i in range(n + 1):
            if i + 1 != nums[i]:
                return [nums[i], i + 1 ]
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         dup = -1
#         for i in range(n):
#             index = abs(nums[i]) - 1
#             if nums[index] < 0 :
#                 dup = abs(nums[i])
#             else:
#                 nums[index] *= -1
#             print(nums)
#         missing = -1
#         for i in range(n):
#             if nums[i] > 0:
#                 missing = i + 1
#         return [dup, missing]
    
