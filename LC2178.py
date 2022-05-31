class Solution:
    def maximumEvenSplit(self, f: int) -> List[int]:
        if f % 2 != 0 or f < 2:
            return []
        
        ans = []
        i = 2
        while f >= i:
            ans.append(i)
            f -= i
            i += 2
        ans[-1] += f
        return ans
