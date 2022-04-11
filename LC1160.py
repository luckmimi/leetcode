class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0 
        for w in words:
            need = collections.Counter(chars)
            cur = 0 
            for c in w:
                if c not in need or need[c] == 0:
                    cur = 0 
                    break
                need[c] -= 1
                cur += 1
            res += cur
        return res
                
                
