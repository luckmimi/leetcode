class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        s = ''
        e = ''
        i = 0
        j = 0
        pos1 = []
        pos2 = []
        for i in range(len(start)):
            if start[i] != 'X':
                pos1.append((start[i],i))
            if end[i] != 'X':
                pos2.append((end[i],i))
        
        if len(pos1) != len(pos2):
            return False
        for i in range(len(pos1)):
            c, p1 = pos1[i]
            e, p2 = pos2[i]
            if (c == 'L' and p1 < p2) or (c =='R' and p1 > p2) or c != e:
                return False
        
    
        return True
            
