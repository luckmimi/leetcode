class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = []
        for val in s.split(" "):
            if val != '':
                arr.append(val)
        
        return ' '.join(arr[::-1])
                
