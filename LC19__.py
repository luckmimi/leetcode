# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        x = self.findN(dummy, n+1)
        x.next = x.next.next
        return dummy.next
        
        
    def findN(self,head,n):
        p1 = head
        for i in range(n):
            p1 = p1.next
        
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
#         def remove(head,n)
#             dummy = ListNode(-1)
#             dummy.next = head
#             fast,slow = dummy,dummy
#             for i in range(n+1):
#                 fast = fast.next
#             while fast:
#                 slow = slow.next
#                 fast = fast.next

#             slow.next = slow.next.next
#             return dummy.next
        
            
