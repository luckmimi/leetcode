class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1,0]] for _ in range(length) ]
        #self.arr = [[[-1,0]] *length ]
        # print(self.arr)
        # print(self.arr1)
        self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        # [[[-1, 0], [-1, 0]]] 1
        # print(self.arr,index)
        # print(self.arr[index])
        self.arr[index].append([self.snap_id, val])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect.bisect(self.arr[index],[snap_id + 1]) - 1
        return self.arr[index][pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
