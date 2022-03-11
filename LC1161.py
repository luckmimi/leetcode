# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        if not root:
            return root
        from queue import Queue
        q = Queue()
        q.put(root)
        depth = 0
        res = 1
        while not q.empty():
            level = 0 
            n = q.qsize()
            depth += 1
            for i in range(n):
                cur = q.get()
                level += cur.val
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
          
            if ans < level:
                res = depth
                ans = level
            
        return res
