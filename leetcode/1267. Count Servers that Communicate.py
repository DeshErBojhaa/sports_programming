# 1267. Count Servers that Communicate
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = {}, {}
        cnt, r, c = 0, len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if not grid[i][j]:
                    continue
                cnt += 1
                row[i] = row.get(i, 0) + 1
                col[j] = col.get(j, 0) + 1
        
        bad = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    if row.get(i, 0) < 2 and col.get(j, 0) < 2:
                        bad += 1
        
        return cnt - bad
