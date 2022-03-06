class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'
        
        s = sentence.split(' ')
        for i in range(len(s)):
            if s[i][0] in vowels:
                s[i] += 'ma'
            else:
                s[i] = s[i][1:] + s[i][0] + 'ma' 
        cnt = 1        
        for i in range(len(s)):
            s[i] += 'a'*cnt
            cnt += 1
        res = ' '.join(s)
                
        
        return res
