# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        n, m = len(matrix), len(matrix[0])
        
        flow = [[0] * m for _ in range(n)]
        ans = []
        
        def fill(r, c, fill_val, already_filled_with):
            if flow[r][c] in already_filled_with:
                return
            
            flow[r][c] |= fill_val
            if flow[r][c] == 3:
                ans.append([r,c])
                
            for nr, nc in ((r, c-1), (r-1, c), (r, c+1), (r+1, c)):
                if nr < 0 or nr >= n or nc < 0 or nc >= m or matrix[r][c] > matrix[nr][nc]:
                    continue
                fill(nr, nc, fill_val, already_filled_with)
        
        for i in range(m):
            fill(0, i, 1, [1])
        for i in range(n):
            fill(i, 0, 1, [1])
            
        for i in range(m):
            fill(n-1, i, 2, [2, 3])
        for i in range(n):
            fill(i, m-1, 2, [2, 3])
        
        return ans
