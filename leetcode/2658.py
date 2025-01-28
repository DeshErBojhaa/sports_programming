class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def fill(r, c):
            if not 0 <= r < R or not 0 <= c < C or grid[r][c] == 0:
                return 0
            
            ans = grid[r][c]
            grid[r][c] = 0
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                ans += fill(nr, nc)
            return ans
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, fill(i, j))
        return ans
