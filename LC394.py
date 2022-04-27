class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        cur_num, cur_str = '', ''
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isnumeric():
                cur_num += c
            elif c.isalpha():
                cur_str += c
            elif c == '[':
                stack.append(cur_str)
                stack.append(int(cur_num))
                cur_str = ''
                cur_num = ''
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + num * cur_str
        return cur_str
                
