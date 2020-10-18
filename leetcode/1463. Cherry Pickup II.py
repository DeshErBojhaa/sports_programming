# 1463. Cherry Pickup II
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        @lru_cache(maxsize=None)
        def rec(row, col1, col2):
            if col1 < 0 or col1 == C or col2 < 0 or col2 == C:
                return float('-inf')
            if row == R-1:
                val = grid[row][col1]
                if col1 != col2:
                    val += grid[row][col2]
                return val
            
            ret = grid[row][col1]
            if col1 != col2:
                ret += grid[row][col2]
            
            val = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    val = max(val, rec(row+1, col1+i, col2+j))
            
            return ret + val
        
        return rec(0, 0, C-1)
            
