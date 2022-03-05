class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(len(nums)-1):
            left.append(left[-1]*nums[i])
        right = 1
        res = [1]*len(nums)
        # print(left)
        for i in range(len(nums)-1,-1,-1):
            res[i] =  left[i]* right
            right *= nums[i]
            
        return res 
            
            
