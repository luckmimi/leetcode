class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0]*n
        for a,b in pre:
            graph[b].append(a)
            indegree[a] += 1
        q = collections.deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        res = 0
        path = []
        while q:
            res += 1
            cur = q.popleft()
            path.append(cur)
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if res == n:
            return path
        return []
            
            
