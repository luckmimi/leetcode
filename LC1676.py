# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        group = set()
        for node in nodes:
            group.add(node.val)
        return self.lca(root,group)
    def lca(self,root,group):
        if not root: return None
        if root.val in group:
            return root
        left = self.lca(root.left, group)
        right = self.lca(root.right, group)
        if left and right:
            return root
        return left or right
            
        
