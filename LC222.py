# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 完全二叉树 的两个子树，至少一棵树是🈵️二叉树
        #计算二叉树的节点个树不用一个个节点去数数，而是直接可以通过树的高度计算出来，这也是这道题的提高效率的关键点
        l, r = root, root
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes(root.left)  + self.countNodes(root.right)
        
#     def countNodes(self, root: Optional[TreeNode]) -> int:
        
#         if not root: return 0
#         if not root.left and not root.right: return 1
#         res = 0
#         left = self.countNodes(root.left)
#         right = self.countNodes(root.right)
       
#         return left + right + 1
