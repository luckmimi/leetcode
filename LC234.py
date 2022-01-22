# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res == res[::-1]
        prev = None
        dummy = ListNode(-1)
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        if fast:
            slow = slow.next
        cur = prev
        
        while slow and cur:
            print(slow.val,cur.val)
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
     
        return True
