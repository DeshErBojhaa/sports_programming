# 1240. Tiling a Rectangle with the Fewest Squares
class Solution:
    d = {}
    def tilingRectangle(self, n: int, m: int) -> int:
        # grid = tuple([tuple([True] * m) for _ in range(n)])
        L = max(n, m)
        
        def fill(g, i, j, k, v):
            for x in range(i, i+k+1):
                for y in range(j, j+k+1):
                    g[x][y] = v
            
        
        # @lru_cache(None)
        def rec(grid, cnt):
            if (grid, cnt) in Solution.d:
                print('Found')
                return Solution.d[grid, cnt]
            if cnt < 0:
                return inf
            
#             print('   '* (L - cnt + 1), cost)
#             for r in grid:
#                 print('   '* (L - cnt + 1), r)
#             print()
            if all(map(all, grid)):
                # print('Returnoing')
                return 0
            
            t = deepcopy(grid)
            grid = list(map(list, grid))
            ans = inf
            for i in range(n):
                found = False
                for j in range(m):
                    if grid[i][j]:
                        continue
                    # new_empty = deepcopy(list(map(list, empty)))
                    for k in range(L+1):
                        if i + k >= n or j + k >= m or grid[i+k][j+k] or grid[i][j+k] or grid[i+k][j]:
                            break
                        fill(grid, i, j, k, 1)
                        ans = min(ans, rec(tuple(map(tuple, grid)), cnt-1) + 1)
                        fill(grid, i, j, k, 0)
                    found = True
                    break
                if found:
                    break
            
            Solution.d[t, cnt] = ans
            return ans
        
        n, m = max(n, m), min(n, m)
        if m == 1:
            return n
        return rec(tuple([tuple([0] * m) for _ in range(n)]), min(n, 7))
