# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        val = preorder[0]
        if len(preorder) == 1:
            return TreeNode(val)
        root = TreeNode(val)
        leftrootval = preorder[1]
        index = postorder.index(leftrootval)
        leftsize = index + 1
        root.left = self.constructFromPrePost(preorder[1:leftsize+1],postorder[:index+1])
        root.right = self.constructFromPrePost(preorder[leftsize+1:],postorder[index+1:-1])
        return root
