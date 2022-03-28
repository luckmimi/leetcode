# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        self.ans = []
        self.ans.append(root.val)
        self.leftboundary(root.left)
        self.leaves(root.left)
        self.leaves(root.right)
        self.rightboundary(root.right)
        return self.ans
    def leftboundary(self,root):
        if not root or (root.left == root.right == None):
            return
        self.ans.append(root.val)
        if not root.left:
            self.leftboundary(root.right)
        else:
            self.leftboundary(root.left)
    
    def leaves(self,root):
        if not root:
            return
        if root.left == root.right == None:
            self.ans.append(root.val)
            return
        
        self.leaves(root.left)
        self.leaves(root.right)
    
    def rightboundary(self,root):
        if not root or (root.left == root.right == None):
            return
        
        if not root.right:
            self.rightboundary(root.left)
        else:
            self.rightboundary(root.right)
        self.ans.append(root.val)
