class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["."] * n for _ in range(n)]
        def is_valid(row,col,board):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j += 1
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j -= 1               
            return True
        def backtrack(row, board):
            if row == len(board):
                tmp = []
                for i in range(len(board)):
                    tmp.append( ''.join(board[i][:]))
                self.res.append(tmp)
                return 
            for col in range(len(board)):
                if not is_valid(row, col,board):
                    continue
                board[row][col] = 'Q'
                backtrack(row + 1, board)
                board[row][col] = '.'
                
            
                
    
        backtrack(0,board)
        return self.res
