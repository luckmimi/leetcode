class DLinkedNode():
    def __init__(self):
        self.key = 0 
        self.value = 0 
        self.prev = None
        self.next = None

class LRUCache():
    # always add the new node right after the head
    def _add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node 
        self.head.next = node
    def _remove_node(self,node):
        # remove an exising node from the linked list
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    def _move_to_head(self,node):
        # move certain node in between to the head
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        # pop the cureent tail
        res = self.tail.prev
        self._remove_node(res)
        return res
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0 
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        
    def get(self, key: int) -> int:
        node = self.cache.get(key,None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
 
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key,None)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
    



# from collections import OrderedDict
# class LRUCache(OrderedDict):
   
#     def __init__(self, capacity: int):
#        self.capacity = capacity
        
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.remove_to_end(key)
#         return self[key]
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.remove_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last = False)
            


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.remove_to_end(key)
#         return self[key]
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.remove_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#                self.popitem(last = False)
