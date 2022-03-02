class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
     
        self.res = 0
        presum = {}
        presum[0] = -1
        prev = 0 
        for i in range(len(nums)):
            prev += nums[i]
            
            if prev - k in presum:
                self.res = max(self.res, i - presum[prev - k] )
            presum[prev] = presum.get(prev,i)
            
        print(presum)
        return self.res
            
