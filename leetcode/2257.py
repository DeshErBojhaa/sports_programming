class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        g = [[0] * n for _ in range(m)]
        for a, b in walls:
            g[a][b] = "#"
        
        for a,b in guards:
            for x in range(b + 1, n):
                if g[a][x] == '#' or g[a][x] == 'G' or (g[a][x] & 1) == 1:
                    break
                g[a][x] |= 1
            for x in range(b-1, -1, -1):
                if g[a][x] == '#' or g[a][x] == 'G' or (g[a][x] & 1) == 1:
                    break
                g[a][x] |= 1
            
            for y in range(a + 1, m):
                if g[y][b] == '#' or g[y][b] == 'G' or (g[y][b] & 2) == 1:
                    break
                g[y][b] |= 2
            
            for y in range(a - 1, -1, -1):
                if g[y][b] == '#' or g[y][b] == 'G' or (g[y][b] & 2) == 1:
                    break
                g[y][b] |= 2
            g[a][b] = 'G'
          
        ans = 0
        for x in g:
            ans += x.count(0)
            
        return ans
