class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
            res = ''
            start = 0
            pos = 0
            mp = {v: k  for k, v in enumerate(indices)}
           
                
            while pos < len(s):
                if pos not in mp:
                    res += s[pos]
                    pos += 1
                    continue
                index = mp[pos]
                source = sources[index]
                target = targets[index]
                substr = s[pos:len(source) + pos]
                    
                if substr == source:
                    res += target
                else:
                    res += substr
                pos += len(source)
       
            
            return res
                    
                        
                    
