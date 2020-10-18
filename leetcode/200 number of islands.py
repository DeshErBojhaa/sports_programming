class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C, ans = len(grid), len(grid[0]), 0
        
        def fill(r, c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c] != '1':
                return
            grid[r][c] = 'X'
            for i, j in zip([0, -1, 0, 1], [-1, 0, 1, 0]):
                fill(r+i, c+j)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    ans += 1
                    fill(i,j)
        return ans
