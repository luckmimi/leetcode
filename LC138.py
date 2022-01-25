"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur :
            map[cur].next = map.get(cur.next,None)
            map[cur].random = map.get(cur.random,None)
            cur = cur.next
        return map.get(head,None)
