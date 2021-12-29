# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        from queue import Queue
        # BFS
        if not nestedList: return 0
        res = 0 
        q = Queue(maxsize = 0) 
        q.put(nestedList)
        depth = 1
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                for nest in cur:
                    if nest.isInteger():
                        res += nest.getInteger() * depth
                    else:
                        q.put(nest.getList())
            depth += 1
        return res
            
        
        
        #DFS
#         self.sm = 0
#         if not nestedList:
#             return 0
        
#         self.helper(nestedList,1)
#         return self.sm
#     def helper(self,nestedList,depth):
        
#         for nest in nestedList:
#             if nest.isInteger():
#                 self.sm += nest.getInteger() * depth
#             else:
#                 self.helper(nest.getList(),depth + 1)
      
                
            
