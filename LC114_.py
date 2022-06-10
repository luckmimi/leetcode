# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        left_side = self.flatten(root.left)
        right_side = self.flatten(root.right)
        root.left = None
        root.right = left_side
        p = root
        while p.right:
            p = p.right
        p.right = right_side
        return root 
#         if not root:return
#         node = root
#         while node:
#             if node.left:
#                 rightmost = node.left
#                 while rightmost.right:
#                     rightmost = rightmost.right
#                 rightmost.right = node.right
#                 node.right = node.left
#                 node.left = None
                
