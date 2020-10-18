# 1254. Number of Closed Islands
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        
        def sink(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c]:
                return
            grid[r][c] = 1
            list(map(sink, [r+1,r-1,r,r], [c,c,c+1,c-1]))
            return
        
        for i in range(R):
            sink(i, 0)
            sink(i, C-1)
        
        for i in range(C):
            sink(0, i)
            sink(R-1, i)
        
        ans = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    ans += 1
                    sink(i, j)
        
        return ans
