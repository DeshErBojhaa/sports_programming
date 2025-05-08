class Solution:
    def minTimeToReach(self, MT: List[List[int]]) -> int:
        N, M = len(MT), len(MT[0])
        cost = [[inf] * M for _ in range(N)]
        cost[0][0] = 0
        q = [[0, 0, 0, 1]]

        while q:
            tm, x, y, d = heappop(q)
            if cost[N-1][M-1] < inf:
                return cost[N-1][M-1]
            for nx, ny in [[x-1,y], [x,y-1],[x+1, y],[x,y+1]]:
                if not 0 <= nx < N or not 0 <= ny < M:
                    continue
                ttt = tm
                print(nx, ny)
                if ttt <= MT[nx][ny]:
                    ttt = MT[nx][ny]
                dx = 2 - d
                if ttt + dx >= cost[nx][ny]:
                    continue
                cost[nx][ny] = ttt + dx
                heappush(q, [cost[nx][ny], nx, ny, 1-d])
        return cost[N-1][M-1]
