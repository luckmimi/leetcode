"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0 
        def dfs(root):
            if not root: return 0
            max_1 = 0 
            max_2 = 0 
            for child in root.children:
                curr = dfs(child) + 1
                if curr > max_1:
                    max_1,max_2 = curr,max_1
                elif curr > max_2:
                        max_2 = curr
                        
                self.res = max(self.res,max_1 + max_2)
            return max_1
            
            
        dfs(root)
        return self.res
        
