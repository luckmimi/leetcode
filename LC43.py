class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        l1 = len(num1)
        l2 = len(num2)
        res = [0]*( l1 + l2)
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                x, y = int(num1[i]), int(num2[j])
                pos1 = i + j 
                pos2 = i + j + 1
                sm = x * y + res[pos1]*10 + res[pos2]
                res[pos1] = sm//10
                res[pos2] = sm % 10
        
        ans = ''
        for i in range(len(res)):
            if len(ans) == 0 and res[i] ==0:
                continue
            else:
                ans += str(res[i])
        if len(ans) ==0:
            return '0'
        else:
            return ans
                
    
            
            
            
                
