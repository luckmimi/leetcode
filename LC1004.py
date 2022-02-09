class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        l, r,zeros = 0 ,0 ,0 
        res = 0 
        while r < len(A):
            if A[r] == 1:
                r += 1
            elif zeros < k:
                zeros += 1 - A[r]
                r += 1
            else:
                zeros -= 1-A[l]
                l += 1
            res = max(res, r-l)
        return res
        # l = 0 
        # zeros = 0 
        # for r in range(len(A)):
        #     if A[r] == 0:
        #         zeros += 1
        #     if zeros > k:
        #         zeros -= 1  - A[l]
        #         l += 1
        # return r - l + 1
