class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        #A = [[0] * len(points) for _ in range(len(points[0]))]
        for i in range(len(A)-1):
            for j in range(len(A[0])-2, -1, -1):
                A[i][j] = max(A[i][j], A[i][j+1] - 1)
            for j in range(len(A[0])):
                A[i][j] = max(A[i][j],A[i][j-1] - 1 if  j else 0)
                A[i+1][j] += A[i][j]
        
        return max(A[-1])
                                              
