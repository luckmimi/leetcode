class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = res = 0 
        for i,f in enumerate(flips, 1):
            right = max(right,f)
            res += right == i 
        return res
#         arr = [0 for _ in range(len(flips))]
#         ans = 0 
#         for i,f in enumerate(flips):
#             arr[f-1] = 1
            
#             if self.valid(arr,i):
#                 ans += 1
#         return ans
#     def valid(self,arr,i):
#         return sum(arr[:i+1]) == (i+1) and sum(arr[i+1:]) == 0
        
            
