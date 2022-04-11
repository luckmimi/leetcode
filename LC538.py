# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sm = 0 
        self.traverse(root)
        
        return root
    def traverse(self,root):
        if not root:return 0
        self.traverse(root.right)
        self.sm += root.val
        root.val = self.sm
        self.traverse(root.left)
        
