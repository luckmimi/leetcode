class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        email_account_map = defaultdict(list)
        
        visited = [False] * len(accounts)
        for i in range(len(accounts)):
            name = accounts[i]
            for email in name[1:]:
                email_account_map[email].append(i)
        def dfs(i,emails):
            if visited[i]:
                return
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for neighbor in email_account_map[email]:
                    dfs(neighbor,emails)
        res = []
        for i in range(len(accounts)):
            if visited[i]:
                continue
            name = accounts[i][0]
            emails = set()
            dfs(i,emails)
            res.append([name]+sorted(emails))
        return res
