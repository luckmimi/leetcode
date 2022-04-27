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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total_sum, level_sum = 0, 0 
        while nestedList:
            next_level_list = []
            for ele in nestedList:
                if ele.isInteger():
                    level_sum += ele.getInteger()
                else:
                    # for a in ele.getList():
                        next_level_list.extend(ele.getList())
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum
    
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         stack = []
#         self.max_depth = 1
#         def put_list_to_stack(lst, depth):
#             self.max_depth = max(self.max_depth, depth)
#             for element in lst:
#                 if element.isInteger():
#                     stack.append((element.getInteger(),depth))
#                 else:
#                     put_list_to_stack(element.getList(),depth + 1)
#         put_list_to_stack(nestedList,1)
#         total = 0 
#         while stack:
#                 val, depth = stack.pop()
#                 total += (val * (self.max_depth - depth + 1))
#         return total
        
        
