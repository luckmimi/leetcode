class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed = 0 
        def val(missed,res,k):
            while missed < k:
                res += 1
                missed += 1
            return res
        for i in range(len(arr)):
            if i == 0:
                missed = arr[0] - 1
                if missed >= k:
                    return k
            else:
                missed += arr[i] - arr[i-1] - 1
                if missed >= k:
                    missed -= arr[i] - arr[i-1] -1
                    res = arr[i-1]
                    return val(missed,res,k)
        return val(missed,arr[-1],k)
                
            
            
            
