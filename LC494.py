class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        self.res = set()
        s = [0]*len(nums)
        s[-1] = nums[-1]
        memo = collections.defaultdict()
        for i in range(len(nums)-2,-1,-1):
            
            s[i] = nums[i] + s[i+1]
        def backtrack(nums, pos,sm,target):
            res = 0 
            if pos == len(nums):
                if  target == sm:
                    res += 1
                return res
            if s[pos] < abs(target - sm) :return 0
            key = f'{pos},{sm}'
            if key in memo:
                return memo[key]
            result = backtrack(nums, pos + 1, sm + nums[pos],target)+ backtrack(nums,pos + 1, sm - nums[pos],target)
            memo[key] = result
                
            return result
            
            
        
        return backtrack(nums,0,0,target)
