class TicTacToe:

    def __init__(self, n: int):
        self.cols = [0]*n
        self.rows = [0]*n
        self.size = n
        self.diagnoal = 0
        self.antiDiagnoal = 0

    def move(self, row: int, col: int, player: int) -> int:
        toAdd = 1 if player == 1 else -1
        self.cols[col] += toAdd
        self.rows[row] += toAdd
        if col == row:
            self.diagnoal += toAdd
        
        
        if col == len(self.cols) - row - 1:
            self.antiDiagnoal += toAdd
            
        if abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(self.diagnoal) == self.size or abs(self.antiDiagnoal) == self.size:
        
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
