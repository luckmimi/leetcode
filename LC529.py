class Solution: 
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        row,col = click
        if board[row][col] == 'M' or board[row][col] == 'X':
            board[row][col] = 'X'
            
            return board
        self.dfs(board,row,col)
        return board
    
    
    def dfs(self,board,x,y):
        if board[x][y] != 'E': return
        dirs = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        nums = 0
        for dx,dy in dirs:
            newx = dx + x
            newy = dy + y
            
            if newx >=0 and newy >= 0 and newx < len(board) and newy < len(board[0]) and board[newx][newy] == 'M':
                    nums += 1
        if nums == 0 :
                board[x][y] = 'B'
        else:
                board[x][y] = str(nums)
                return
        
        for dx,dy in dirs:
            newx = dx + x
            newy = dy + y
            if 0<= newx < len(board) and 0<=newy < len(board[0]):
                self.dfs(board,newx,newy)
     
        

         
                
