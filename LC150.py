class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = "+-*/"
        for token in tokens:
            if token in operand:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack.pop()
