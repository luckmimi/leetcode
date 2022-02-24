"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev = head
        succ = head.next
        while True:
            if prev.val <= insertVal <= succ.val:
                break
            if prev.val > succ.val and (prev.val < insertVal or succ.val > insertVal):
                break
            prev = succ
            succ = succ.next
            if prev == head:
                break
        newN = Node(insertVal)
        newN.next = succ
        prev.next = newN
        return head
