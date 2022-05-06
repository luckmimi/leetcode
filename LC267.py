class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        dd = [0] * 26
      
        for char in s:
            dd[ord(char) - ord('a')] += 1
        cnt = 0 
        for i in range(26):
            if dd[i] % 2 == 1:
                cnt += 1
                odd = i
        if cnt > 1:
            return []
        if cnt == 1:
            base = chr(odd + ord('a'))
            size = len(s) - 1
            dd[odd] -= 1
        else:
            base = ''
            size = len(s)
        
        self.res = []
        self.backtrack( base, size,dd)
        return self.res
    def backtrack(self,base,size,dd):
            if size == 0:
                self.res.append(base)
                return
            
            for i in range(26):
                
                if dd[i] == 0:
                    continue
                dd[i] -= 2
                char = chr(i + ord('a'))
                
                self.backtrack(char + base+ char, size - 2,dd)
                dd[i] += 2
                
    
            
                
        
