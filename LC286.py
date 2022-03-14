class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0 :
                    self.helper(rooms,i, j,0)
                    
    def helper(self,rooms,i,j,dst):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or (dst != 0 and rooms[i][j] <=dst):
            return
        rooms[i][j] = dst
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dt,dy in directions:
            self.helper(rooms,i + dt,j + dy, dst + 1)
        
