class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.strip()
#         arr = []
#         for val in s.split(" "):
#             if val != '':
#                 arr.append(val)
        
#         return ' '.join(arr[::-1])
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
