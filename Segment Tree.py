class STreeNode:
    def __init__(self, start, end, x):
        self.start = start
        self.end = end
        self.interval_sum = x
        self.left = self.right = None
class SegementTree:
    def __inti__(self, nums, start, end):
        self.root = self.cosntruct(nums, start, end)
    def construct(self, nums, start, end):
        if start > end:
            return None
        new_node = STreeNode(start, end, 0)
        if start != end:
            mid = start + (end - start) // 2
            new_node.left = self.construct(nums, start, mid)
            new_node.right = self.construct(nums, mid + 1, end)
            if new_node.left:
                new_node.interval_sum += new_node.left.interval_sum
            if new_node.right:
                new_node.interval_sum += new_node.right.interval_sum
        else:
            new_node.interval_sum = nums[start]
        return new_node
