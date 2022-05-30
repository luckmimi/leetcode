class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        indegree = {}
        res = []
        for i in range(len(recipes)):
            cur = recipes[i]
            indegree[cur] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(cur)
              
        q = collections.deque(supplies)
        ans = []
        while q:
            rec = q.popleft()
            if rec in recipes:
                ans.append(rec)
            for ind in graph[rec]:
                indegree[ind] -= 1
                if indegree[ind] == 0:
                    q.append(ind)
        return ans
