# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = collections.defaultdict(int)
        res = []
        def traverse(root):
            if not root:
                return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subTree = left + "," + right + "," + str(root.val)
            freq = seen.get(subTree,0)
            if freq == 1:
                res.append(root)
            seen[subTree] += 1
            return subTree
        traverse(root)
        return res
        
