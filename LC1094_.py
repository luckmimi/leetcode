class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 1001
        diff = [0] * n
        res = [0] * n
        for num, i, j in trips:
            diff[i] += num
            if j  < n:
                diff[j] -= num
        res[0] = diff[0]
        if res[0] > capacity:
            return False
        for i in range(1,n):
            res[i] = res[i-1] + diff[i]
            if res[i] > capacity:
                return False
        return True
