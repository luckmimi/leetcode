# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0 
        for other in range(1, n):
            if knows(cand, other) or not knows(other,cand):
                cand = other
        for other in range(n):
            if other == cand:
                continue
            if not knows(other,cand) or knows(cand, other):
                return -1
        return cand
