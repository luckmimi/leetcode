class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, row, col, word):
                    return True
        return False
    def backtrack(self,board,row, col, word):
            if len(word) == 0 :
                return True
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 or board[row][col] != word[0]:
                return False
            ret = False
            board[row][col] = '#'
            for dx , dy in ((0,1),(0,-1),(-1,0),(1,0)):
                ret = self.backtrack(board, row + dx, col + dy,word[1:])
                if ret:
                    break
            board[row][col] = word[0]
            
            return ret
                                             
        
            
