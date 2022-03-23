# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.successor = None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reversed(head,right)
        head.next = self.reverseBetween(head.next,left-1,right-1)
        return head
    def reversed(self,head,n):
        
        if n==1:
            self.successor = head.next
            return head
        last = self.reversed(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last
        
#         if not head: return
#         dummy = ListNode(-1)
#         prev = dummy
#         prev.next = head
#         for i in range(1,left):
#             prev = prev.next
            
#         curr = prev.next  # 2  prev: 1
#         for i in range(left,right):
#             print(f'cur:{curr.val}',end = ',')
#             tmp = curr.next  # 3
#             curr.next = tmp.next
#             tmp.next = prev.next
#             prev.next = tmp  # 1 - > 3   
#             print(curr.val)
#         return dummy.next
            
            
