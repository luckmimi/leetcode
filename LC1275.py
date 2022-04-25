class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0 
        player = 1
        for row, col in moves:
            rows[row] += player
            cols[col] += player
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
            if any(abs(line) == n for line in (rows[row],cols[col],diag,anti_diag)):
                return 'A' if player == 1 else 'B'
            player *= -1
        return 'Draw' if len(moves) == n * n else 'Pending'
#         self.n = 3
#         self.board = [[0] *self.n for _ in range(self.n)]
#         player = 1
#         for move in moves:
#             row, col = move
#             self.board[row][col] = player
#             if self.checkRow(row,player)  or self.checkCol(col,player) or (col == row and self.checkDiagnoal(player)) or ( col + row == self.n - 1  and self.checkAntiDiagnoal(player)):
#                 return 'A' if player == 1 else 'B'
            
#             player *= -1
#         return 'Draw' if len(moves) == self.n * self.n else 'Pending'
                
#     def checkRow(self,row, player_id):
#         for col in range(self.n):
#             if self.board[row][col] != player_id:
#                 return False
#         return True
    
#     def checkCol(self,col, player_id):
#         for row in range(self.n):
#             if self.board[row][col] != player_id:
#                 return False
#         return True
    
#     def checkDiagnoal(self,player_id):
#         for row in range(self.n):
#             if self.board[row][row] != player_id:
#                 return False
#         return True
#     def checkAntiDiagnoal(self,player_id):
#         for row in range(self.n):
#             if self.board[row][self.n- 1 - row] != player_id:
#                 return False
#         return True
