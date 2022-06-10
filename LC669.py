# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 二叉树的递归可以分为遍历和分解问题 两种思路，这道题用到 分解问题 的思维
        # 明确了递归函数的定义之后进行思考，如果一个节点没有落在【low，high】中，有两种情况：
        # 1 root.val < low, 这种情况root本身节点 以及root的左子树 全部小于low，都需要被剪掉
        # root.val > high, 这种情况root本身节点以及root的右子树，全部大于high，都需要剪掉
        if not root: return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
