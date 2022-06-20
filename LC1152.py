class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pair = collections.defaultdict(list)
        for (u, i, t)  in zip(username, website, timestamp):
            pair[u].append((t,i))
        for k,v in pair.items():
            tmp = sorted(v, key = lambda x : x[0])
            pair[k] = tmp
        self.combine = collections.defaultdict(set)
        for key, value in pair.items():
            tmp = [v for t, v in value]
            if len(tmp) < 3:
                continue
            if len(tmp) == 3:
                self.combine[tuple(tmp)].add(key)
            else:
              
                self.backtrack(tmp,0,[],key)
    
        
        mx = max([len(i) for i in self.combine.values()])
        res = []
       
        for key in self.combine:
            if len(self.combine[key]) == mx:
 
                res.append(list(key))
                
        # print(sorted(res)[0])
        return sorted(res)[0]
    def backtrack(self,t,pos,cur,key):
        if len(cur) == 3:
            self.combine[tuple(cur)].add(key)
            return
            
        for i in range(pos, len(t)):
            self.backtrack(t, i  + 1, cur + [t[i]],key)
            
