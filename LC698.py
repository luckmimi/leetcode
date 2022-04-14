class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums): return False
        if sum(nums) % k != 0: return False
        target  = sum(nums) / k
        self.memo = {}
        used = 0 
        return self.backtrack(k,0,nums,0,used,target)
    def backtrack(self,k, bucket, nums,start, used, target):
        if k == 0: return True
        if bucket == target:
            res = self.backtrack(k - 1,0, nums, 0,used, target)
            self.memo[used] = res
            return res
        if used in self.memo:
            return self.memo[used]
        
        for i in range(start, len(nums)):
            if (used >> i & 1) == 1 : # 1&1 == 0, 0 &1 == 0  判断i是否为1
                continue
            if nums[i] + bucket > target: continue
            used |= 1 << i #将i设为1
            # print(used)
            bucket += nums[i]
            #递归下个数据是否可以放入当前痛
            if self.backtrack(k,bucket,nums,i+1,used,target):
                return True
            used ^= 1 << i # 将位置i设为0
            bucket -= nums[i]
        return False
