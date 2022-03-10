class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        left = 0 
        right = len(nums) - 1
        i = len(nums) -1
        while left <= right:
            if nums[right]**2 >= nums[left]**2:
                ans[i] = nums[right]**2
                right -= 1
                
            else:
                ans[i] = nums[left]**2
                left += 1
            i -= 1
        return ans
