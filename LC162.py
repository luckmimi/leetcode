class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
       
        l = 0 
        r = len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            else:
                if nums[mid] > nums[mid +1]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l if nums[l] > nums[r] else r
        
