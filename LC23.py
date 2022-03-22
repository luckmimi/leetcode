# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        h = []
        i = 0 
        for item in lists:
            if item:
                h.append((item.val,i,item))
                i += 1
        heapq.heapify(h)
        dummy = ListNode(-1)
        cur = dummy
       
        while h:
            val,_,Node = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = Node.next
            if node:
                heapq.heappush(h,(node.val,i,node))
                i += 1
        return dummy.next
