from queue import SimpleQueue       
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C, ans = len(grid), len(grid[0]), 0
        Q = SimpleQueue()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    Q.put((i,j,0))
        
        while Q.qsize():
            rc = Q.get()
            for i, j in zip([0,-1,0,1], [-1,0,1,0]):
                ni, nj = rc[0]+i, rc[1]+j
                if ni < R and ni >=0 and nj < C and nj >= 0:
                    if grid[ni][nj] == 1:
                        ans = max(ans, rc[2]+1)
                        grid[ni][nj] = 2
                        Q.put((ni,nj,rc[2]+1))
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1
        return ans
