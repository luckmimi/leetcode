class TicTacToe:

    def __init__(self, n: int):
        self.col = [0] * n
        self.row = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        toAdd = 1 if player == 1 else - 1
        self.row[row] += toAdd
        self.col[col] += toAdd
        if row == col:
            self.diagonal += toAdd
        if row + col == self.n - 1:
            self.antidiagonal += toAdd
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiagonal) == self.n:
            return player
        return 0 
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
