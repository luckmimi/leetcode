
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        print(visited)
        color = [False ]* len(graph)
        self.ok = True
        for i in range(len(graph)):
                if not visited[i]:
                    self.bfs(graph,i,visited,color)
                        
        return self.ok
        
    def bfs(self,graph, v,visited,color):
        if not self.ok:
            return 
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                color[w] = not color[v]
                self.bfs(graph,w,visited,color)
            else:
                if color[v] == color[w]:
                    self.ok = False
      
                  
