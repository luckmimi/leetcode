class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(nums,target,leftBias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = left + (right - left) //2
                if nums[mid]> target:
                    right = mid - 1
                elif nums[mid] < target:
                        left = mid + 1
                else:
                    i = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
           
            
            return i
        
        left = search(nums,target,True)
        right = search(nums,target,False)
        return [left,right]
                    
           
        
