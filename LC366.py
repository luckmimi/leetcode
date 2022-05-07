# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = collections.defaultdict(list)
        self.maxDepth(root)
        return self.res.values()
    def maxDepth(self,root):
        if not root:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        h = max(left, right) + 1
        if h not in self.res:
            self.res[h]= [root.val]
        else:
            self.res[h].append(root.val)
        return h
    
