# 1559. Detect Cycles in 2D Grid
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        N, M = len(grid), len(grid[0])
        
        dis = [[0]*M for _ in range(N)]
        
        def dfs(r, c, char, last = 0):
            if not 0 <= r < N or not 0 <= c < M:
                return False
            if grid[r][c] != char:
                return False
            
            nonlocal dis
            
            if dis[r][c]: 
                return last - dis[r][c] >= 3
            
            dis[r][c] = last + 1
            
            for nr, nc in [[r,c+1], [r,c-1], [r+1,c], [r-1,c]]:
                if not 0 <= nr < N or not 0 <= nc < M:
                    continue
                if grid[nr][nc] != char:
                    continue
                if dfs(nr, nc, char, last+1):
                    return True
            
            return False
        
        for i in range(N):
            for j in range(M):
                if dis[i][j]:
                    continue
                # dis[i][j] = 1
                if dfs(i,j, grid[i][j]):
                    # for d in dis:
                    #     print(d)
                    return True
    
        return False

# ["f","a","a","c","b"],
# ["e","a","a","e","c"],
# ["c","f","b","b","b"],
# ["c","e","a","b","e"],
# ["f","e","f","b","f"]
