# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def traverse(root):
            if not root:
                return 0 
            left = max(0,traverse(root.left))
            right = max(0,traverse(root.right))
            self.res = max(self.res, left + right + root.val )
           
            return max(left, right) + root.val
            
        traverse(root)
        return self.res
        
