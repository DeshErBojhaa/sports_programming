class Solution:
    def minTimeToReach(self, MT: List[List[int]]) -> int:
        N, M = len(MT), len(MT[0])
        q = [[0, 0, 0]]
        ans = [[inf] * M for _ in range(N)]
        ans[0][0] = 0
        while q:
            if ans[-1][-1] < inf:
                return ans[-1][-1]
            tm, x, y = heappop(q)
            for nx, ny in [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]:
                if not 0 <= nx < N or not 0 <= ny < M:
                    continue
                tt = tm
                if tt <= MT[nx][ny]:
                    tt = MT[nx][ny]
                if tt + 1 >= ans[nx][ny]:
                    continue
                ans[nx][ny] = tt + 1
                heappush(q, [tt + 1, nx, ny])
        return ans[-1][-1]
