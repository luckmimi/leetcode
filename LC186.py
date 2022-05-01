class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left,right):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        reverse(0,len(s)-1)
        left = 0 
        for index, char in enumerate(s):
            if char == ' ':
                reverse(left,index - 1)
                left = index + 1
        reverse(left, len(s) - 1)
            
#         if len(s) == 1:
#             return s
        
#         left = 0 
#         right = len(s) - 1
#         while left < right:
#             if s[right] != ' ' and s[left] != '':
# #                 s[right],s[left] = s[left], s[right]
# #                 right -= 1
#                 left += 1
    
                
