class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1, r1_revert = grid[0], [1 - i for i in grid[0]]
        for i in range(1,len(grid)):
            if grid[i] != r1 and grid[i] != r1_revert:
                return False
        return True 
