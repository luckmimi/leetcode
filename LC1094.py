class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 1001
        diff = [0]* n
        for val,i,j in trips:
            diff[i] += val
            if j < n:
                diff[j] -= val
        res =[0]*n
        res[0] = diff[0]
        
        for i in range(1,n):
            res[i] = res[i-1] + diff[i]
            if res[i] > capacity:
                return False
        if res[0] > capacity:
            return False
        return True
