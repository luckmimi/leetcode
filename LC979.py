# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res  = 0 
        self.getRest(root)
        return self.res
    def getRest(self,root): # 定义： 输入一颗二叉树，返回这颗二叉树中多出来的硬币个数，返回负数 代表缺少硬币
        if not root:
            return 0
        left = self.getRest(root.left)
        right = self.getRest(root.right)
        # 让当前这颗树平衡所需要的移动次数
        self.res += abs(left) + abs(right) + (root.val - 1)
        #实现函数的定义
        return left + right + root.val - 1
