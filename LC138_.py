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
        if not head: 
            return head
        mp = collections.defaultdict()
        cur = head
        while cur:
            val = cur.val
            mp[cur] = Node(val,None,None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mp[cur].next = mp[cur.next]
            if cur.random:
                mp[cur].random = mp[cur.random]
            cur = cur.next
        return mp[head]
