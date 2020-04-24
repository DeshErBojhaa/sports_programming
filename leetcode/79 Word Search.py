class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return
        R, C = len(board), len(board[0])
        
        ans = False
        def find(ind, r,c):
            nonlocal ans, board
            if ind == len(word):
                ans = True
                return
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[ind]:
                return
            if board[r][c] == '#':
                return
            
            board[r][c] = '#'
            
            for i, j in zip([0,-1,0,1], [-1,0,1,0]):
                if ans:
                    return
                find(ind+1, r+i, c+j)
                
            board[r][c] = word[ind]
        
        for i, b in enumerate(board):
            if ans:
                return True
            for j, c in enumerate(b):
                if ans:
                    return True
                if c == word[0]:
                    find(0, i, j)
        return ans
