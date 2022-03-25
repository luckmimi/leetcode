# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      
        if not preorder:
            return 
        val = preorder[0]
        index = inorder.index(val)
        leftsize = index
        root = TreeNode(val)

        root.left = self.buildTree(preorder[1:leftsize + 1],inorder[:index])
        root.right = self.buildTree(preorder[leftsize + 1:],inorder[index+1:])
        
        return root
