# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from queue import Queue
        q = Queue(maxsize = 0 )
        q.put((root,1))
        res = 0
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                cur,depth = q.get()
                #print(cur.val,depth,end = ',')
                if cur.left:
                    if cur.left.val == cur.val+1:
                        tmp = depth  + 1
                    else:
                        tmp = 1
                    q.put((cur.left,tmp ))
                if cur.right:
                    if cur.right.val == cur.val + 1:
                        tmp = depth  + 1
                    else:
                        tmp = 1
                    q.put((cur.right,tmp ))
                
                res = max(res, depth )
           
        return res
