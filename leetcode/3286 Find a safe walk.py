class Solution:
    def findSafeWalk(self, grid: List[List[int]], hh: int) -> bool:
        r, c = len(grid), len(grid[0])
        inf = 1000000000
        seen = [[inf] * c for _ in range(r)]
        seen[0][0] = grid[0][0]
        q = deque([(0, 0, grid[0][0])])

        while q:
            i, j, h = q.popleft()
            if i == r-1 and j == c-1:
                xx = h + grid[i][j]
                seen[i][j] = min(seen[i][j], xx)


            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i+di, j+dj

                if 0 <= ni < r and 0 <= nj < c:
                    nh = grid[ni][nj] + h
                    if nh < seen[ni][nj]:
                        seen[ni][nj] = nh
                        q.append((ni, nj, nh))

        # for s in seen:
        #     print(*s)
        return seen[r-1][c-1] < hh
