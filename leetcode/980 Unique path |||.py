class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        vis = [[False]*C for _ in range(R)]
        
        empty, start, end = 0, None, None
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    empty += 1
                    start = (i,j)
                elif grid[i][j] == 2:
                    empty += 1
                    end = (i,j)
        
        def rec(i, j, fill, flag):
            if (i,j) == end:
                if fill == empty:
                    return 1
                return 0
            
            flag[i][j] = True
            cur = 0
            for r,c in zip([0,-1,0,1], [-1,0,1,0]):
                if i+r<0 or i+r>= R or j+c <0 or j+c>=C:
                    continue
                if grid[i+r][j+c] == -1:
                    continue
                if flag[i+r][j+c]:
                    continue
                cur += rec(i+r, j+c, fill+1, flag)
            flag[i][j] = False
            return cur
        vis[start[0]][start[1]] = True
        return rec(start[0], start[1], 1, vis)
