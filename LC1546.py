class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
       
        res = 0
        seen =set()
        pref = 0 
        seen.add(0)
        for i in range(len(nums)):
            pref += nums[i]
            
            if pref - target in seen:
                res += 1
                seen = set()
            seen.add(pref)
        return res
            
                
