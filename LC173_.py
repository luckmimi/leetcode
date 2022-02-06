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
            if A[p1][1] < B[p2][0]:
                p1 += 1
            elif A[p1][0] > B[p2][1]:
                    p2 += 1
            else:
                res.append([max(A[p1][0],B[p2][0]),min(A[p1][1],B[p2][1])])
                if A[p1][1] == B[p2][1]:
                    p1 += 1
                    p2 += 1
                else:
                    if A[p1][1] < B[p2][1]:
                        p1 += 1
                    else:
                        p2 += 1
        return res
                       
