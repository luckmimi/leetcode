class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        heights = [x[1] for x in envelopes]
        #return self.lengthOfLIS(heights)
        return self.dp(heights)
    def dp(self,nums):
        res = float('-inf')
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(dp[i],res)
        
        return res
            
        
    
    def lengthOfLIS(self,arr):
        top = [0] * len(arr)
        piles = 0 
        for i in range(len(arr)):
            poker = arr[i]
            # left insert position
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] < poker:
                    left = mid + 1
                else: 
                    right = mid
            if left == piles:
                piles += 1
            top[left] = poker
        return piles
                
                    
