# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > p.val:
            successor = self.inorderSuccessor(root.left,p)
            if not successor:
                successor = root
        if root.val < p.val:
            successor = self.inorderSuccessor(root.right,p)
        if root.val == p.val:
            successor = self.getMin(root.right)
        return successor
    def getMin(self,root):
        while root and root.left:
            root = root.left
        return root
        
        
        # # def traverse(root):
        #     if not root:
        #         return None
        #     if root.val > p.val:
        #         successor = self.inorderSuccessor(root.left,p)
        #         return successor if successor else root
        #     return self.inorderSuccessor(root.right,p)
