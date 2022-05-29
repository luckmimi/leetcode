class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        m = []
        res = float('inf')
        for n in timePoints:
            a,b =  n.split(":")
            m.append(int(a)*60+int(b))
       
        m.sort()
        m.append(m[0]+1440)
        return min([b-a for a,b in zip(m,m[1:])])
