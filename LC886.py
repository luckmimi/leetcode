class Solution:
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [False] * (n + 1)
        color = [False] * (n + 1)
        self.ok = True
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(1, n + 1):
            if not visited[i]:
                # self.bfs(graph, i, visited, color)
                self.dfs(graph, i, visited, color)
        return self.ok
    def bfs(self, graph, start, visited, color):
        q = collections.deque([])
        q.append(start)
        while q and self.ok:
            cur = q.popleft()
            for nei in graph[cur]:
                if not visited[nei]:
                    color[nei] = not color[cur]
                    visited[nei] = True
                    q.append(nei)
                    
                else:
                    if color[nei] == color[cur]:
                        self.ok = False
    def dfs(self, graph, cur, visited, color):
        if visited[cur]:
            return 
        visited[cur] = True
        for nei in graph[cur]:
            if not visited[nei]:
                color[nei] = not color[cur]
                self.dfs(graph, nei, visited, color)
                    
            else:
                if color[nei] == color[cur]:
                    self.ok = False
    
        
    
