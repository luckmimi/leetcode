class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        self.res =[]
        def backtracking(c,pos,left, cur):
            if left == 0:
                self.res.append(cur.copy())
                return
            elif left < 0:
                return
            for i in range(pos,len(c)):
                
                backtracking(c,i,left - c[i],cur + [c[i]])
                
        
        backtracking(c,0,target,[])
        
        return self.res
