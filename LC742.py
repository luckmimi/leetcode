# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = collections.defaultdict(list)
        def dfs(node,par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        q = collections.deque(node for node in graph if node and node.val == k)
        seen = set(q)
        while q:
            node = q.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
