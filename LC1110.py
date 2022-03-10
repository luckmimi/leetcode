# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        d = set(to_delete)
        def check(root):
            if not root: return None
            cur = root.val
            root.left = check(root.left)
            root.right = check(root.right)
            if cur in d:
                if root.left:
                    # if root.left.val not in d:
                    #     ans.append(root.left)
                    ans.append(root.left)
                if root.right:
                    # if root.right.val not in d:
                    #     ans.append(root.right)
                    ans.append(root.right)
                # if not root.left and not root.right:
                return None

            return root
        check(root)
        if root and root.val not in d:
            ans.append(root)
        return ans
                    
