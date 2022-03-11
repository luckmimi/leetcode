class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(list)
        for i in range(len(equations)):
            a,b = equations[i]
            edges[a].append((b,values[i]))
            edges[b].append((a,1.0/values[i]))
        print(edges)
        clusters = []
        visit = set()
        for (a,b) in equations:
            dict = {}
            if a not in visit:
                start = a
                visit.add(a)
                dict[a] = 1
                q = [start]
                while q:
                    cur = q.pop()
                    for x, val in edges[cur]:
                        if x not in visit:
                            visit.add(x)
                            q.append(x)
                            dict[x] = dict[cur]*val
            clusters.append(dict)
        ans = []    
        for a,b in queries:
                for cluster in clusters:
                    if a  in cluster and b in cluster:
                        ans.append(cluster[b]/cluster[a])
                        break
                else:
                    ans.append(-1)
        return ans
