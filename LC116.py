"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        cur = root
        while cur:
            head = cur
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = head.left
        return root
        
