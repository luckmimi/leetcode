      class STreeNode:
    def __init__(self,start, end, x):
        self.start = start
        self.end = end
        self.interval_min = x
        self.left = self.right = None
        
class SegmentTree:
    def __init__(self,nums, start, end):
        self.root = self.construct(nums, start, end)
    def construct(self, nums, start, end):
        if start > end:
            return None
        node = STreeNode(start,end,float('inf'))
        if start != end:
            mid = start + (end - start) // 2
            node.left = self.construct(nums, start, mid)
            node.right = self.construct(nums, mid + 1, end)
            if node.left:
                node.interval_min = min(node.interval_min,node.left.interval_min)
            if node.right:
                node.interval_min = min(node.interval_min, node.right.interval_min)
        else:
            node.interval_min = nums[start]
        return node
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.interval_min = value
            return
        mid = root.start + (root.end - root.start) // 2
        if root.start <= index <= mid:
            self.modify(root.left, index, value)
            node.interval_min = min(node.interval_min,node.left.interval_min)
        if mid < index <= root.end:
            self.modify(root.right, index, value)
            node.interval_min = min(node.interval_min,node.right.interval_min)
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.interval_min
        mid = root.start + (root.end  - root.start) // 2
        res =  float('inf')
        if start <= mid < end:
            res = min(res,self.query(root.left, start, mid),self.query(root.right, mid + 1, end))
        elif start > mid:
            res =min(res, self.query(root.right, start, end))
        elif end <= mid:
            res = min(res, self.query(root.left, start, end))
        return res
