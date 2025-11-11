# # class STreeNode:
# #     def __init__(self, start, end, val):
# #         self.start = start
# #         self.end = end 
# #         self.interval_sum = val
# #         self.left = None 
# #         self.right = None 
# # class SegmentTree:
# #     def __init__(self, nums, start, end):
# #         self.root = self.construct_tree(nums, start, end)
# #     def construct_tree(self, nums, start, end):
# #         if start == end:
# #             return  STreeNode(start, end, nums[start])
        
# #   

class SegmentNode:
    def __init__(self, l, r, merge_val):
        self.l = l 
        self.r = r 
        self.merge_val = merge_val 
        self.left = None 
        self.right = None 
class DynamicsSegmentTree:
    def __init__(self, start, end, merger, default_value):
        self.merger = merger
        self.default_value = default_value
        self.root = SegmentNode(start, end, default_value)
    def init_children_if_needed(self, node):
        if node.l == node.r:
            # left node, no need to create children node
            return 
        mid = node.l + (node.r - node.l) // 2
        if node.left is None:
            node.left = SegmentNode(node.l, mid, self.default_value)
        if node.right is None:
            node.right = SegmentNode(mid + 1, node.r, self.default_value)
    def update(self, index, value):
        self._update(self.root, index, value)
    def _update(self, node, index, value):
        if node.l == node.r == index:
            node.merge_val = value 
            return 
        self.init_children_if_needed(node)
        mid = node.l + (node.r - node.l) // 2
        if index <= mid:
            self._update(node.left, index, value)
        else:
            self._update(node.right, index, value)
        node.merge_val = self.merger(node.left.merge_val, node.right.merge_val)
    def query(self, l, r):
        if l > r:
            raise ValueError('invalid query range')
        return self._query(self.root, l, r)
    def _query(self, root, l, r):
        if root.l == l and root.r == r:
            return root.merge_val
        mid = root.l + (root.r - root.l) // 2
        if r <= mid:
            return self._query(root.left, l, r)
        elif l > mid:
            return self._query(root.right, l, r)
        return self.merger(self._query(root.left, l, mid), self._query(root.right, mid + 1, r))
class NumArray:

    def __init__(self, nums: List[int]):
        self.sg = DynamicsSegmentTree(0, len(nums) - 1, lambda x, y : x + y, 0)
        for i in range(len(nums)):
            self.sg.update(i, nums[i])
        

    def update(self, index: int, val: int) -> None:
        self.sg.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sg.query(left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
