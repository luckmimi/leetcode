class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        if len(nums) == 1:
            return res
        stack = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > stack[-1]:
                # pos = binary(nums,nums[i])
                stack.append(nums[i])
            else:
                pos = self.find(stack,nums[i])
                stack[pos] = nums[i]
            
                
        return len(stack)
    def find(self,sub,target):
        left = 0 
        right = len(sub) - 1
        while left + 1 < right:
            mid = left + (right - left) //2
            if sub[mid]<= target:
                left = mid
            else:
                right = mid 
        if sub[left] >= target:
            return left
        return right
        
