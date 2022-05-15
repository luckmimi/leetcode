class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, weight in times:
                graph[start].append( (end,weight))
        if k not in graph:
            return -1
        return self.bfs(graph,k, n)
    def bfs(self,graph,k,n):
        q = collections.deque([(k,0)])
        distance = {k:0}
        while q:
            cur,cur_dst = q.popleft()
            for nei,dst in graph[cur]:
                tmp =  dst + cur_dst
                if nei not in distance or distance[nei] > tmp:
                    distance[nei] = tmp
                    q.append((nei,tmp))
        if len(distance.keys()) == n:
            return max(distance.values())
        
        return -1
    
