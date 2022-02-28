class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                
                if sm == target:
                    return sm
                if abs(sm - target) < abs(res - target):
                    res = sm
                if sm > target:
                    right -= 1
                else:
                    left += 1
        return res
