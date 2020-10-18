# 688. Knight Probability in Chessboard
from functools import lru_cache
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        sr, sc = r, c
        @lru_cache(maxsize=None)
        def rec(r, c, move):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0.
            if move == K:
                return 1.
            
            ans = 0
            
            for dr, dc in zip([-2,-1,1,2,2,1,-1,-2], [-1,-2,-2,-1,1,2,2,1]):
                nr, nc = r + dr, c + dc
                ans += rec(nr, nc, move+1) * (1/8.)
            
            return ans
        
        ans = rec(sr, sc, 0)
        return ans
