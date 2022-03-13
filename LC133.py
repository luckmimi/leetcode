"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # if the node was already visited before
        # return the clone from the viisted dictionary
        if node in self.visited:
            return self.visited[node]
        
        
        # create a clone for the given node
        # Note that we do not have cloned neighbors as of row, hence[]
        clone_node = Node(node.val,[])
        
        self.visited[node] = clone_node 
        # the key through the neighbors to generate their clones
        # and prepare a list of a cloned neighbors to be added to the cloned node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node
