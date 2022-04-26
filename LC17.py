class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.res = []
        if len(digits) == 0:
            return self.res
        self.backtrack(digits,0, '')
        return self.res
    def backtrack(self,digits, start, sb):
            if len(sb) == len(digits):
                self.res.append(sb)
                return 
            for i in range(start, len(digits)):
                d = int(digits[i])
                for c in self.mapping[d]:
                    self.backtrack(digits, i + 1, sb + c)
                    
     
            
