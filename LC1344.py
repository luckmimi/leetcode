class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 360/12 
        m = 360/60
        # if hour == 12:
        #     hour = 0 
        res =  abs(minutes * m - h *(hour + minutes/60))
        return min(res,360-res)
