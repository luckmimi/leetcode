# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.q = 0 
        self.p = 0
        def dfs(root,p,q):
            if not root: return
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            if root.val == p.val:
                self.p += 1
                return root
            if root.val == q.val:
                self.q += 1
                return root
            if left and right:
                return root
            return left or right
            
        res = dfs(root,p,q)
      
        if self.q and self.p:
                return res
        return None
                
