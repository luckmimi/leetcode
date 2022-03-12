# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        from queue import Queue
        q = Queue(maxsize = 0)
        q.put(root)
        while not q.empty():
            n = q.qsize()
            level = []
            for i in range(n):
                cur = q.get()
                level.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            ans.append(max(level))
        return ans 
