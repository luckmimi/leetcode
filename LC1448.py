# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0 
        def dfs(root, max_path):
            if not root:
                return 
            if root.val >= max_path:
                self.res += 1
                
            max_path = max(root.val, max_path)
            dfs(root.left, max_path )
            dfs(root.right,max_path)
        
        dfs(root,float('-inf'))
        return self.res
                
