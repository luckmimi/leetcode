# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(root,res):
            if not root:
                return 
            res = res * 10 + root.val
            if not root.left and not root.right:
                self.res += res
            dfs(root.left,res)
            dfs(root.right,res)
        
        dfs(root,0)
        return self.res
