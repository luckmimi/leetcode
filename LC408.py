class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        p2 = 0
        
        while p1 < len(word) and p2 < len(abbr) :
            if abbr[p2].isnumeric():
                if abbr[p2] == '0':
                    return False
                else:
                    tmp = ''
                    while p2 < len(abbr) and abbr[p2].isnumeric():
                        tmp += abbr[p2]
                        p2 += 1
                    p1 += int(tmp)
            else:
                if word[p1] != abbr[p2]:
                    return False
                else:
                    p1 += 1
                    p2 += 1
       
        return p1 == len(word)  and p2 == len(abbr)
    
