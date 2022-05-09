class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        self.backtrack(wordDict, 0,[],s)
        return self.res
    def backtrack(self,wordDict,i,track,s):
        if i == len(s):
            self.res.append(" ".join(track))
            return 
        if i > len(s):
            return
        for word in wordDict:
            if i + len(word) > len(s): continue
            if s[i: i + len(word)] != word: continue
            self.backtrack(wordDict, i + len(word),track + [word],s)
