# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.results = 0 
        def helper(root,cur_max, cur_min):
            if not root:
                return
            self.results = max(self.results,abs(cur_max - root.val),abs(cur_min-root.val ))
            cur_max = max(cur_max,root.val)
            cur_min = min(cur_min,root.val)
            helper(root.left,cur_max,cur_min)
            helper(root.right,cur_max,cur_min)
        helper(root,root.val,root.val)
        return self.results
