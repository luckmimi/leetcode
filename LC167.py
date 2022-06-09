class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        res = []
        while left < right:
            sm = nums[right] + nums[left]
            if sm == target:
                return [left + 1, right + 1]
            elif sm > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
            
            
