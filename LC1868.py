class Solution:
    def findRLEArray(self, e1: List[List[int]], e2: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        res = []
        while a < len(e1) and b < len(e2):
            
            if res and res[-1][0] == e1[a][0]*e2[b][0]:
                    
                    res[-1][1] += min(e1[a][1],e2[b][1])
            else:
                
                    res.append([ e1[a][0]*e2[b][0],min(e1[a][1],e2[b][1])])
    
            x = min(e1[a][1],e2[b][1])
        
            e1[a][1] -= x
            e2[b][1] -= x
            
            if e1[a][1] == 0:
                a += 1
            if e2[b][1] == 0:
                b += 1          
           
       
        return res
                
