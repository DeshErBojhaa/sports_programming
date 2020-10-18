class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        def fill(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if board[i][j] != 'O':
                return
            
            board[i][j] = '.'
            fill(i+1, j)
            fill(i-1, j)
            fill(i, j+1)
            fill(i, j-1)
        
        # Left
        for i in range(len(board)):
            if board[i][0] == 'O':
                fill(i,0)
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                fill(0,i)
        for i in range(len(board[0])):
            if board[len(board)-1][i] == 'O':
                fill(len(board)-1, i)
        # Right
        for i in range(len(board)):
            if board[i][len(board[0])-1] == 'O':
                fill(i, len(board[0])-1)
        
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
