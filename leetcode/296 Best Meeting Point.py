from functools import reduce
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                rows.append(i)
                cols.append(j)
        
        n = len(rows)
        rows.sort()
        cols.sort()
        
        ans = 0
        for r in rows:
            ans += abs(rows[n//2] - r)
        
        for c in cols:
            ans += abs(cols[n//2] - c)
        
        return ans
