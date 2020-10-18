class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.N = n
        self.top_down = [0] * n
        self.left_right = [0] * n
        self.zig = 0
        self.zag = 0
        
        self.zig_pos = set((i,j) for i, j in zip(range(n), range(n)))
        self.zag_pos = set((i,j) for i, j in zip(range(n), range(n-1, -1, -1)))
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        f = 1 if player == 1 else -1
        self.top_down[col] += f
        if abs(self.top_down[col]) == self.N:
            return player
        self.left_right[row] += f
        if abs(self.left_right[row]) == self.N:
            return player
        if (row, col) in self.zig_pos:
            self.zig += f
        if abs(self.zig) == self.N:
            return player
        if (row, col) in self.zag_pos:
            self.zag += f
        if abs(self.zag) == self.N:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
