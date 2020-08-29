# 741. Cherry Pickup
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        
        @lru_cache(None)
        def rec(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (not (0 <= r1 < N and 0 <= r2 < N)) or (not (0 <= c1 < M and 0 <= c2 < M)):
                return -math.inf
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -math.inf
            if r1 == r2 and c1 == c2 and r1 == N-1 and c2 == M-1:
                return grid[N-1][M-1]
            
            ans = grid[r1][c1] + (grid[r2][c2] if (r1 != r2 or c1 != c2) else 0)
            
            gain = -math.inf
            for d1, d2 in product([(0,1), (1,0)], [(0,1), (1,0)]):
                nr1, nc1 = r1 + d1[0], c1 + d1[1]
                nr2, nc2 = r2 + d2[0], c2 + d2[1]

                gain = max(gain, rec(nr1, nc1, nc2))
            
            return ans + gain
        
        ans = rec(0,0,0)
        return max(0, ans)
