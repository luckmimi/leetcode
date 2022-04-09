# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        prev, a, b = None, head, head
        for i in range(k):
            if not b: return head
            b = b.next
            
        newhead = self.reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return newhead
    def reverse(self,a,b):
        prev = None
        cur = a
        while cur != b:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
