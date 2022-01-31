class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            while l<= r and  not s[l].isalnum():
                l += 1
            while l<= r and  not s[r].isalnum():
                r -= 1
            if l<= r and s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
