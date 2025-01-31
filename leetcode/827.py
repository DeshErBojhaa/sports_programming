class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sz = [[None] * m for _ in range(n)]
        ids = [[None] * m for _ in range(n)]

        def rec(i, j):
            if sz[i][j] is not None:
                return sz[i][j]
            sz[i][j] = 1
            mx = 1
            for ni, nj in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
                if not 0 <= ni < n or not 0 <= nj < m or sz[ni][nj] is not None:
                    continue
                if grid[ni][nj] == 0:
                    continue
                mx += rec(ni, nj)
            return mx
        
        _id = 0
        def fill(i, j, val):
            if ids[i][j] is not None:
                return
            sz[i][j] = val
            ids[i][j] = _id
            for ni, nj in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
                if not 0 <= ni < n or not 0 <= nj < m:
                    continue
                if grid[ni][nj] == 0:
                    continue
                if sz[ni][nj] >= val:
                    continue
                fill(ni, nj, val)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                mx = rec(i, j)
                if mx == n * m:
                    return mx
                fill(i, j, mx)
                _id += 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                tmp = 1
                seen = set()
                for ni, nj in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
                    if not 0 <= ni < n or not 0 <= nj < m or grid[ni][nj] == 0:
                        continue
                    if ids[ni][nj] in seen:
                        continue
                    tmp += sz[ni][nj]
                    seen.add(ids[ni][nj])
                ans = max(ans, tmp)
        return ans
