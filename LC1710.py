class Solution:
    def maximumUnits(self, box: List[List[int]], truckSize: int) -> int:
        box.sort(key = lambda x: -x[1])
        res = 0
        cur_size = 0
        print(box)
        for num_box, unit in box:
            
            res += unit * min(truckSize - cur_size, num_box)
            cur_size += min(truckSize - cur_size, num_box)
            print(res, cur_size,)
            
        return res
