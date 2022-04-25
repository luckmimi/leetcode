class Solution:
    def calculate(self, s: str) -> int:

        def helper(s):
            stack = []
            num = 0 
            sign = '+'
            while len(s) > 0:
                c = s.popleft()
                if c == "(":
                    num = helper(s)
                if c.isnumeric():
                    num = num * 10 + int(c)
                if (not c.isnumeric() and c != ' ') or ( len(s) == 0):
                    if sign == '+' :
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack[-1] *= num
                    if sign == '/':
                        stack[-1] = int(stack[-1]/num)
                    sign = c
                    num = 0 
                if c == ')':
                    break
            return sum(stack)
        
        return helper(collections.deque(s))
