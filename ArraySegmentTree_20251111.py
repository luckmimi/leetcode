from typing import Callable
class ArraySegmentTree:
    # using array to construct 
    def __init__(self, nums:list[int], merge:Callable[[int, int], int]):
        self.n = len(nums)
        self.merge = merge
        self.tree = [0] *( 4 * self.n)
        self.build(nums, 0, self.n - 1, 0)
    def build(self, nums, l, r, root_index:int):
        if l == r:
            self.tree[root_index] = nums[l]
            return
        mid = l + (r - l) // 2
        left_root_index = self.left_children(root_index)
        right_root_index = self.right_children(root_index)
        self.build(nums, l, mid, left_root_index)
        self.build(nums, mid + 1, r, right_root_index)
        self.tree[root_index] = self.merge(self.tree[left_root_index], self.tree[right_root_index])
    def update(self, index, value):
        self._update(0, self.n - 1, 0, index, value)
    def _update(self, l, r, root_index, index, value):
        if l == r:
            self.tree[root_index] = value 
            return 
        mid = l + (r - l)// 2
        if index <= mid:
            self._update(l, mid, self.left_children(root_index), index, value)
        else:
            self._update(mid + 1, r, self.right_children(root_index), index, value)
        self.tree[root_index] = self.merge(self.tree[self.left_children(root_index)], self.tree[self.right_children(root_index)])
    def query(self, left, right):
        if left < 0 or right > self.n - 1 or left > right:
            raise ValueError(f'invalid range:[{left}, {right}]')
        return self._query(0, self.n - 1, 0, left, right)
    def _query(self, l, r, root_index, left, right):
        if l == left and right == r:
            return self.tree[root_index]
        mid = l + (r - l)// 2
        left_root_index = self.left_children(root_index)
        right_root_index = self.right_children(root_index)
        if right <= mid:
            return self._query(l, mid, left_root_index, left, right)
        elif left > mid:
            return self._query(mid + 1, r, right_root_index, left, right)
        else:
            return self.merge(self._query(l, mid, left_root_index, left, right), self._query(mid + 1, r, right_root_index, left, right))
    def left_children(self, pos):
        return pos * 2 + 1
    def right_children(self, pos):
        return pos * 2 + 2
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    # 示例，创建一棵求和线段树
    st = ArraySegmentTree(arr, lambda a, b: a + b)

    print(st.query(1, 3)) # 3 + 5 + 7 = 15
    st.update(2, 10)
    print(st.query(1, 3)) # 3 + 10 + 7 = 20
