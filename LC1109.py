class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        
        diff = [0]*n
        for i, j, val in bookings:
            diff[i-1] += val
            if j < n:
                diff[j] -= val
        res = [0]*n
        res[0] = diff[0]
        for i in range(1,n):
            res[i] = res[i - 1] + diff[i]
        return res
