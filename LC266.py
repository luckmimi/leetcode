class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        count = Counter(s)
        res = 0
        for value in count.values():
            if value % 2 == 1:
                res += 1
        return res <= 1
