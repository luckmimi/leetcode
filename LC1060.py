class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                
                cnt += nums[i] - nums[i-1] - 1
                # print(cnt)
            if cnt == k:
                # print(cnt)
                return nums[i] - 1
            else:
                    if cnt > k:
                        cnt -=  nums[i] - nums[i-1] - 1
                        j = nums[i-1]
                        while cnt < k and j < nums[i]:
                            cnt += 1
                            j += 1
                        return j
            
        return nums[-1] + k - cnt 
        
                            
