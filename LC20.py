class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c in map:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if map[stack[-1]] != c:
                        return False
                    else:
                        stack.pop()
        return stack ==[]
                
