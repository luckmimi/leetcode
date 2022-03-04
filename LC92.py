# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(-1)
        prev = dummy
        prev.next = head
        for i in range(1,left):
            prev = prev.next
            
        curr = prev.next  # 2  prev: 1
        for i in range(left,right):
            tmp = curr.next  # 3
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp  # 1 - > 3   
            
        return dummy.next
            
