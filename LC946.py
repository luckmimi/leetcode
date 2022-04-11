class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        cur = 0 
        for i in range(len(pushed)):
            val = pushed[i]
            stack.append(val)
            while stack and stack[-1] == popped[cur]:
                    stack.pop()
                    cur += 1
        return cur == len(popped)
                
