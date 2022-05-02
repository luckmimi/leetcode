
    
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = [ 0] * n
        for a, b in pre:
            graph[b].append( a)
            indegree[a] += 1
        q = collections.deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
    
        seen = set()
        res = 0 
        while q:
            res += 1
            cur = q.popleft()
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                   q.append(nei)
                
        return res == n
            
            
