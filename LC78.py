class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtracking(nums,pos,res):
            self.res.append(res.copy())
            for i in range(pos,len(nums)):
                res.append(nums[i])
                backtracking(nums,i + 1,res)
                res.pop()
        
        backtracking(nums,0,[])
        return self.res
