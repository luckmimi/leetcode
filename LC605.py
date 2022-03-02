class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        cnt = 0 
        f.extend([0,0])
        for i in range(len(f)-2):
            if f[i - 1] == f[i] == f[i+1] == 0 :
                f[i] = 1
               
                cnt += 1
    
        return cnt>=n
                
