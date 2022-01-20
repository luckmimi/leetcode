class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        prev = 0
        cur = 0
        for log in logs:
            index, status, time = log.split(':')
            time = int(time)
            index = int(index)
            if status == 'start':
                stack.append([index,time])
            else:
                if stack and  stack[-1][0] ==  index:
                        duration = time- stack[-1][1] + 1
                        res[index] += duration
                        stack.pop()
                        if stack:
                            prevIndex = stack[-1][0]
                            res[prevIndex] -= duration
        
        return res
