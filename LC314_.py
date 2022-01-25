# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        from collections import defaultdict
        col = defaultdict(list)
        
        from queue import Queue
        q = Queue( maxsize = 0 )
        level = 0 
        q.put([root,level])
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                cur,level = q.get()
                col[level].append(cur.val)
                if cur.left:
                    q.put([cur.left,level - 1])
                if cur.right:
                    q.put([cur.right, level + 1])
        
        # print(col)
        return [col[k] for k in sorted(col.keys())]
                
            
        
