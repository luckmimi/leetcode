class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        m = collections.defaultdict(list)
        for a,b in edges:
            m[a].append(b)
            m[b].append(a)
        self.d = 0
        def dfs(cur,visited):
            if cur not in m:
                return
            t1, t2 = 0, 0
            distance = 0 
            visited.add(cur)
            for n in m[cur]:
                if n not in visited:
                    distance = 1 + dfs(n,visited)
                if distance > t1:
                    t1, t2 = distance, t1
                elif distance > t2:
                    t2 = distance
            
            self.d = max(self.d, t1 + t2)
            return t1
        visited = set()
        dfs(0,visited)
        
        return self.d
