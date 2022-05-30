class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda word:len(word))
        res = 0
        dict = {}
        for word in words:
            cur = 1
            for i in range(len(word)):
                w = word[:i] + word[i + 1:]
                if w in dict:
                    cur = max(cur, dict[w] + 1)
            dict[word] = cur
            res = max(res, dict[word])
        return res
