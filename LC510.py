"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # 右子树的最小值就是successor
        p = node.right
        while p and p.left:
            p = p.left
        if p:
            return p
        
        #如果没有柚子树的，第一个比自己大的父亲节点就是successor
        #但是p可能是父节点的坐姿节点也可能是柚子节点
        #但p是做节点的时候父节点才能是successor
        p = node
        while p.parent and p.parent.right == p:
            p = p.parent
        return p.parent
       
