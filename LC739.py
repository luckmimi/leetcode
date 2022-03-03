class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        stack = [(temp[0],0)]
        for i in range(1,len(temp)):
            while stack and  temp[i] > stack[-1][0]:
                cur, index = stack.pop()
                ans[index] = i - index
                
            stack.append((temp[i],i))
      
        return ans
