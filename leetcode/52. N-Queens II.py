# 52. N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        dale, hill = [False] * (2*n), [False] * (2*n)
        cols = [False] * n
        
        def queen_possible(r, c):
            if cols[c] or hill[r+c] or dale[r-c+n]:
                return False
            return True
                
        def fill(row):
            if row == n:
                nonlocal ans
                ans += 1
                return
            
            for i in range(n):
                if queen_possible(row, i):
                    cols[i] = True
                    hill[row+i] = True
                    dale[row-i+n] = True
                    fill(row+1)
                    cols[i] = False
                    hill[row+i] = False
                    dale[row-i+n] = False
        
        fill(0)
        
        return ans
