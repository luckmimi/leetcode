class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0 
            while len(s) > 0:
                cur = s.popleft()
                if cur == "(":
                   num = helper(s)
                if cur.isnumeric():
                    num = num * 10 + int(cur)

                if (not cur.isnumeric() and  cur != ' ') or len(s) == 0 :

                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)

                    num = 0 
                    sign = cur
                if cur == ')':
                        break
            return sum(stack)
        return helper(collections.deque(s))
