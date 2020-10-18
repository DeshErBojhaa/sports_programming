# 51. N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        def queen_possible(queens, x, y):
            for qx, qy in queens:
                if qx == x or qy == y:
                    return False
                if abs(qx - x) == abs(qy - y):
                    return False
            return True
                
        def fill(row, board, queens):
            if row == n:
                ans.append(board[::])
                return
            this_row = ['.'] * n
            for i in range(n):
                if queen_possible(queens, row, i):
                    this_row[i] = 'Q'
                    fill(row+1, board + [''.join(this_row)] , queens + [(row, i)])
                    this_row[i] = '.'
        
        fill(0, [], [])
        
        return ans
