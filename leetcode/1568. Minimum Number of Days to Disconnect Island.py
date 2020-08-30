# 1568. Minimum Number of Days to Disconnect Island
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        
        def flood(i,j, g, col):
            if i < 0 or i >= N or j < 0 or j >= M:
                return
            if g[i][j] == 0 or g[i][j] == col:
                return
            
            g[i][j] = col
            flood(i+1,j, g, col)
            flood(i-1,j, g, col)
            flood(i,j+1, g, col)
            flood(i,j-1, g, col)
            
        
        def disconnected(g):
            # for r in g:
            #     print(r)
            # print()
            ones = sum(row.count(1) for row in g)
            if ones == 0:
                return True
            
            col = 0
            
            for i in range(N):
                for j in range(M):
                    if g[i][j] == col or g[i][j] == 0:
                        continue
                    col -= 1
                    flood(i,j, g, col)
            
            s = set()
            for i in range(N):
                for j in range(M):
                    if g[i][j] == 0:
                        continue
                    s.add(g[i][j])
            
            if len(s) > 1:
                return True
            return False
            
        
        if disconnected(copy.deepcopy(grid)):
            return 0
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dis = disconnected(copy.deepcopy(grid))
                    if dis:
                        return 1
                    grid[i][j] = 1
        return 2
