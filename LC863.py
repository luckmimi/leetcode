# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph, res, visited = collections.defaultdict(list), [], set()
        def build_graph(root):
            if not root:
                return
            if root.left:
                graph[root.left].append(root)
                graph[root].append(root.left)
                build_graph(root.left)
            if root.right:
                graph[root.right].append(root)
                graph[root].append(root.right) 
                build_graph(root.right)
        build_graph(root)
        def find(node,d):
            
            if d < k:
                visited.add(node)
                for n in graph[node]:
                    if n not in visited:
                        find(n,d+1)
            else:
                    res.append(node.val)
        find(target,0)
        return res
                
