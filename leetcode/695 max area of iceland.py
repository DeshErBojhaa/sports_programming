def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m, ans = len(grid), len(grid[0]), -1
        flag = [[False]*m for _ in range(n)]
        
        def chk(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if not grid[i][j]:
                return False
            return True
        
        def trav(i, j):
            if not chk(i,j):
                return 0
            if flag[i][j]:
                return 0

            flag[i][j] = True
            nonlocal ans
            
            a = trav(i+1, j)
            b = trav(i, j+1)
            c = trav(i-1, j)
            d = trav(i, j-1)
            
            grid[i][j] = a + b + c + d + 1
            ans = max(ans, grid[i][j])
            return grid[i][j]
        
        for i in range(n):
            for j in range(m):
                trav(i,j)
        
#        print(grid)
        return max(0, ans)
