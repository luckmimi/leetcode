class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed = set()
        for i in range(len(s)):
            cur = s[i]
            if cur == '(':
                stack.append(i)
            elif cur == ')':
                if stack:
                    stack.pop()
                else:
                    removed.add(i)
        res = ''
        removed = removed.union(set(stack))
        for i in range(len(s)):
            if i not in removed:
                res += s[i]
        return res                
                
 
    
