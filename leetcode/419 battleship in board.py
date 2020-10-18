def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                ans += 1
                # Horizontal battleship
                c = j + 1
                while c < m and board[i][c] == 'X':
                    board[i][c] = '.'
                    c += 1
                    
                r = i + 1
                while r < n and board[r][j] == 'X':
                    board[r][j] = '.'
                    r += 1
                
                board[i][j] = '.'
        
        # print(board)
        return ans
