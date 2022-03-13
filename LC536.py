# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        stack = []
        n = len(s)
        i = 0 
        while i < n:
            if s[i] =='-':
                i += 1
                num = 0 
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(TreeNode(-num))
                i -= 1
            elif s[i].isdigit():
                num = 0 
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(TreeNode(num))
                i -= 1
            
            elif s[i] ==')':
                curNode = stack.pop()
                if stack:
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = curNode
                    else:
                        parent.right = curNode
            i += 1
        return stack[0]
            
