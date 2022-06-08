class TrieNode:
    def __init__(self):
        self.sons = [None, None]
        self.is_num = False
        self.num = 0
    def insert(self, num):
        node = self
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if not node.sons[bit]:
                node.sons[bit] = TrieNode()
            node = node.sons[bit]
        node.is_num = True
        node.num = num
    def get_nearest_num(self, num):
        node = self
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if node.sons[1 - bit]:
                node = node.sons[1 - bit]
            else:
                node = node.sons[bit]
        return node.num
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            root.insert(num)
        max_xor = 0 
        for num in nums:
            tmp = root.get_nearest_num(num)
            max_xor = max(max_xor, tmp ^ num)
        return max_xor
        
