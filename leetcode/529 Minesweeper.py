# 529. Minesweeper
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        
        n, m = len(board), len(board[0])
        q = deque()
        q.append(click)
        
        while q:
            r, c = q.popleft()
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return board
                
            if board[r][c] != 'E':
                continue
            
            bomb_count = 0
            tmp_q = []
            for nr,nc in ((r,c-1), (r-1,c-1), (r-1,c), (r-1, c+1), (r,c+1), (r+1,c+1), (r+1,c), (r+1,c-1)):
                if nr < 0 or nr >=n or nc < 0 or nc >= m:
                    continue
                    
                bomb_count += int(board[nr][nc] == 'M')
                tmp_q.append((nr,nc))
            
            if bomb_count:
                board[r][c] = str(bomb_count)
            else:
                board[r][c] = 'B'
                q.extend(tmp_q)

        
        return board
