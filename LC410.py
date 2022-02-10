class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def valid(nums,mid,m):
            sm = 0
            count = 1
            for val in nums:
                sm += val
                if sm > mid:
                    sm = val
                    count += 1
                if count > m:
                    return False
            return True
        
        left = max(nums)
        right = sum(nums)
        mid = 0 
        while left + 1 < right:
        
            mid = left + (right - left) //2
            if valid(nums,mid,m):
                right = mid
            else:
                left = mid
    
        if valid(nums,left,m):
            return left
        return right
                
        
