class Solution:
    def maxLength(self, r: List[int], k: int) -> int:
        if sum(r) < k:
            return 0
        left = 1
        right = max(r)
        def valid(r,k,mid):
            res = 0
            for i in r:
                res += i//mid
            if res >= k:
                return True
            return False
        while left + 1 < right:
            mid = left + (right - left)//2
            if valid(r,k,mid):
                left = mid
            else:
                right = mid
        if valid(r,k,right):
                return right
       
        return left
      
            
    
