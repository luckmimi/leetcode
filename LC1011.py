class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        def valid(weights,days,ship):
            d = 0 
            curweight = 0 
            for w in weights:
                if w > ship:
                    return False
                if curweight + w > ship:
                    d += 1
                    curweight = w
                else:
                    curweight += w
                if d > days:
                    return False
            d += 1
            return d <= days
        
        left = 1
        right = sum(w)
        while left + 1 < right:
            mid = left + (right - left )//2
            if valid(w,d,mid):
                right = mid
            else:
                left = mid
        
        return left if valid(w,d,left) else right
