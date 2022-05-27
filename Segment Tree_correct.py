class STreeNode:
    def __init__(self, start, end, x):
        self.start = start
        self.end = end
        self.interval_sum = x
        self.left = self.right = None
class SegmentTree:
    def __init__(self, nums, start, end):
        self.root = self.construct(nums, start, end)
    def construct(self, nums, start, end):
        if start > end:
            return None
        node = STreeNode(start, end, 0)
        if start != end:
            mid = start + (end - start) // 2
            node.left = self.construct(nums, start, mid)
            node.right = self.construct(nums, mid + 1, end)
            if node.left:
                node.interval_sum += node.left.interval_sum
            if node.right:
                node.interval_sum += node.right.interval_sum
        else:
            node.interval_sum = nums[start]
        return node
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.interval_sum = value
            return 
        mid = root.start + (root.end - root.start) // 2
        if root.start <= index <= mid:
            self.modify(root.left, index, value)
        if mid < index <= root.end:
            self.modify(root.right, index, value)
        root.interval_sum = root.left.interval_sum + root.right.interval_sum
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.interval_sum
        mid = root.start + (root.end - root.start) // 2
        result = 0 
        if start <= mid < end:
            result += self.query(root.left, start, mid)
            result += self.query(root.right, mid + 1, end)
        elif start > mid:
            result += self.query(root.right, start, end)
        elif end <= mid:
            result += self.query(root.left, start, end)
        return result
            
