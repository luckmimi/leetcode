class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        arr = list(str(num))
        map = {int(d):i for i,d in enumerate(arr)}
        print(map)
        # print(map)
        for i, d in enumerate(arr):
            for j in range(9,int(d),-1):
                if map.get(j,-1) > i:
                    arr[map[j]],arr[i] = d,str(j)
                    # print(arr)
                    return ''.join(arr)
        return num
