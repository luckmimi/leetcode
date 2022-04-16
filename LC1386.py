class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        r.sort()
        seat = collections.defaultdict(set)
        for row, num in r:
            if num in set([2,3,4,5]):
                seat[row].add(0)
            if num in set([4,5,6,7]):
                seat[row].add(1)
            if num in set([6,7,8,9]):
                seat[row].add(2)
        res = 2 * n
        for row in seat:
            if len(seat[row]) == 3:
                res -= 2
            else:
                res -= 1
        return res
