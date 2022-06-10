# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        pos = nums.index(max(nums))
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos + 1 : ])
        return root
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stack = [0] * n
        nodes = []
        for i in range(n):
            node = TreeNode(nums[i])
            nodes.append(node)
            while stack and nums[stack[-1]] < nums[i]:
                node.left = nodes[stack.pop()]
            if stack and nums[stack[-1]] > nums[i]:
                nodes[stack[-1]].right = node
            stack.append(i)
        return nodes[stack[0]]
                
            
