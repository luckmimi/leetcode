# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        def lcs(root,start,dest):
            if not root: return None
            if root.val == start or root.val == dest: return root
            left = lcs(root.left,start, dest)
            right = lcs(root.right, start, dest)
            if left and right:
                return root
            return left or right
           
        node = lcs(root,start,dest)
      
        stack = [(node,'')]
        ps,pd = '',''
        res = ''
        while stack:
           
            node, path = stack.pop()
            if node.val == start: 
                ps = path
            if node.val == dest:
                pd = path
            if node.left:
                stack.append((node.left, path + 'L'))
            if node.right:
                stack.append((node.right, path + 'R'))
        return "U"*len(ps) + pd    
