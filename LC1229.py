class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], duration: int) -> List[int]:
        s1.sort()
        s2.sort()
        p1 = 0 
        p2 = 0 
        while p1 < len(s1) and p2 < len(s2):
            left, right = max(s1[p1][0],s2[p2][0]), min(s1[p1][1],s2[p2][1])
            if right >= left + duration:
                return [left, left + duration]
            else:
                if s1[p1][1] == right:
                    p1 += 1
                else:
                    p2 += 1
                    
        return []
