class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        from sortedcontainers import SortedList, SortedSet, SortedDict
        if len(nums) == 1:
            return False
        pre = {0:-1}
        presum = 0 
        for i in range(len(nums)):
            presum += nums[i]
            if k != 0:
                presum = presum % k
            if presum in pre:
                if i- pre[presum]>= 2:
                    return True
            else:
                pre[presum] = i
        return False
                
