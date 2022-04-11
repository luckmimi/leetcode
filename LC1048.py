class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key = lambda x: len(x))
        m = {}
        res = 0 
        for word in words:
            cur = 1
            for i in range(len(word)):
                tmp = word[:i] + word[i+1:]
                if tmp in m:
                    cur = max(cur, m[tmp] + 1)
            m[word] = cur
            res = max(res, m[word])
        return res
                    
