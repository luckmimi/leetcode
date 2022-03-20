# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      
        def helper(root):
            if not root: return 0,None
            h1,l = helper(root.left)
            h2,r = helper(root.right)
            if h1 > h2: return h1 +1, l
            if h2 > h1: return h2+1,r
            return h1+1, root
        return helper(root)[1]
            
