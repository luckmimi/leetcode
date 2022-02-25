class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if len(words) == 0:
            return s
        flag = [False]*len(s)
        for word in words:
            start = s.find(word)
            end = len(word)
            while start != -1 :
                for i in range(start,start + end):
                    flag[i] = True
                start =   s.find(word,start+ 1)
    
        res = ''
        print(flag)
        i = 0 
        while i < len(s):
            
            if flag[i]:
                res += '<b>'
                while  i < len(s) and flag[i]:
                    res += s[i]
                    i += 1
                
                res += '</b>'
            else:
                res += s[i]
                i += 1
                
        
        return res
                
