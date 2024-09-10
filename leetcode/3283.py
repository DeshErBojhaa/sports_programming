from functools import cache
from typing import List
from collections import deque

M, N, INF = 50, 50, 10**10
moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

def bfs(x, y, target_x, target_y):
    cost = [[INF] * 50 for _ in range(50)]
    q = deque([(x, y)])
    cost[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if cost[nx][ny] > cost[x][y] + 1:
                cost[nx][ny] = cost[x][y] + 1
                q.append((nx, ny))

            if nx == target_x and ny == target_y:
                return cost[nx][ny]
    return INF

class Solution:
    def maxMoves(self, _kx: int, _ky: int, ppp: List[List[int]]) -> int:
        ppp = [[_kx, _ky]] + ppp
        n = len(ppp)
        dist = {}

        for i in range(n):
            for j in range(i+1, n):
                dist[(i, j)] = bfs(*ppp[i], *ppp[j])
                dist[(j, i)] = dist[(i, j)]


        @cache
        def rec(mask, idx, try_max=True):
            if mask == 0:
                return 0

            ans = -INF if try_max else INF
            kx, ky = ppp[idx]
            for i in range(1, n):
                if mask & (1<<i) == 0:
                    continue
                x, y = ppp[i]
                xx = dist[idx, i]
                if try_max:
                    ans = max(ans, rec(mask ^ (1<<i), i, not try_max) + xx)
                else:
                    ans = min(ans, rec(mask ^ (1<<i), i, not try_max) + xx)
            return ans

        msk = ((1<<n) - 1) ^ 1
        return rec(msk, 0)
