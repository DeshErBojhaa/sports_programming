# 289. Game of Life
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        N, M = len(board), len(board[0])
        
        tmp = [[None] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                alive = 0
                for ni, nj in zip([i, i-1, i-1, i-1, i, i+1, i+1, i+1], [j-1,j-1,j, j+1, j+1,j+1,j,j-1]):
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    alive += int(board[ni][nj] == 1 or board[ni][nj] == -5)
                if board[i][j]:
                    if alive < 2 or alive > 3:
                        board[i][j] = -5
                else:
                    if alive == 3:
                        board[i][j] = 5

            
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0 or board[i][j] == -5:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
