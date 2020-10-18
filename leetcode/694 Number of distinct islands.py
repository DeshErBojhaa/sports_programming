class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        R, C = len(grid), len(grid[0])
        
        def get_island(i, j, ti, tj):
            if i >= R or i < 0 or j >= C or j < 0:
                return ()
            if not grid[i][j]:
                return ()
            tup = (i-ti, j-tj)
            grid[i][j] = 0
            for dx, dy in zip([-1,0,1,0], [0,-1,0,1]):
                tup += get_island(i+dx, j+dy, ti, tj)
            return tup
            
        ans = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    island = get_island(i,j, i,j)
                    ans.add(island)
        return len(ans)
