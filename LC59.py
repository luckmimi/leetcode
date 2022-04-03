class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        upper, left = 0, 0 
        lower, right = n - 1, n - 1
        cur = 1 
        while cur <=  n * n :
            if upper <= lower:
                for i in range(left, right + 1):
                    res[upper][i] = cur 
                    cur += 1
                upper += 1
                
            if left <= right:
                for i in range(upper, lower + 1):
                    res[i][right] = cur
                    cur += 1
                right -= 1
            
            if upper <= lower:
                for i in range( right, left - 1, -1):
                    res[lower][i] = cur 
                    cur += 1
                lower -= 1
                
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res[i][left] = cur
                    cur += 1
                left += 1
        return res
                        
