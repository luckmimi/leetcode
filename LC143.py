# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        p = head
        while p:
            lastNode = stack.pop()
            next_node = p.next
            if lastNode == next_node or lastNode.next == next_node:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next_node
            p = next_node
        
                
