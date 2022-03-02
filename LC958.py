# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        from queue import Queue
        if not root:
            return True
        q = Queue()
        q.put(root)
        is_none = False
        while not q.empty():
            cur = q.get()
            if not cur:
                is_none = True
                continue
            if is_none:
                    return False
            q.put(cur.left)
            q.put(cur.right)
        return True
