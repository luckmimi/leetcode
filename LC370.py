class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        def d(length):
            diff = [0]*length
            dfff[0]=nums[0]
            for i in range(1,len(nums)):
                diff[i] = nums[i] - nums[i-1]
            return diff
        
        diff = [0]*length
        res = [0]*length
        
        for i,j, val in updates:
            diff[i] += val
            if j + 1 < length:
                diff[j+1] -= val
     
        res[0] = diff[0]
        for i in range(1,length):
            res[i] = res[i-1] + diff[i]
        
        return res
