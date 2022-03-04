# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return
        from queue import Queue
        q = Queue(maxsize = 0)
        q.put(root)
        while not q.empty():
            n = q.qsize()
            cur = []
            for i in range(n):
                node = q.get()
                cur.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                    
            res.append(sum(cur)/len(cur))
        return res
