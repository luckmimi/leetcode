class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return []
        A.sort()
        B.sort()
        p1 = 0
        p2 = 0 
        res = []
        while p1 <= len(A) - 1 and p2 <= len(B) - 1:
            first = max(A[p1][0],B[p2][0])
            second = min(A[p1][1],B[p2][1])
            if first <= second:
                res.append([first,second])
            if A[p1][1] > second:
                    p2 += 1
            else:
                    p1 += 1
        return res
