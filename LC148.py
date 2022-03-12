# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        arr = []
        def helper(node):
            while node:
                arr.append(node.val)
                node = node.next
                
        helper(head)
        arr.sort()
        dummy = ListNode(-1)
        cur = dummy
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        
        return dummy.next
            
