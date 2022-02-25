# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        M, N = mat.dimensions()
        res = -1
        
        for row in range(M):
            left = 0
            right = res - 1 if res != -1 else N - 1
            while left + 1 < right:
                mid = left + (right - left)//2
                if mat.get(row,mid) == 0:
                    left = mid 
                else:
                    right = mid
            
            if left < M and mat.get(row,left) == 1:
                res = left
            else:
                if right >= 0 and  mat.get(row,right) == 1:
                    res = right
         
        return res
