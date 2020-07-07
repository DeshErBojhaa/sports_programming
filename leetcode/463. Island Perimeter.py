# 463. Island Perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        R, C = len(grid), len(grid[0])
        peri = 0
        
        for i in range(R):
            for j in range(C):
                if not grid[i][j]:
                    continue
                for ni, nj in zip([i-1,i,i+1,i], [j,j+1,j,j-1]):
                    if ni < 0 or ni >= R or nj < 0 or nj >= C or grid[ni][nj] == 0:
                        peri += 1
        
        return peri
