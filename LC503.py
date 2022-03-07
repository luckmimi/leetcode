class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        res = [-1] *len(nums) 
        for i in range(len(nums) -1,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res
        
