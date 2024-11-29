class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        N, M = len(grid), len(grid[0])
        cost, heap = [[inf] * M for _ in range(N)], [[0, 0, 0, 0]]
        cost[0][0] = 0

        while heap:
            c, s, i, j = heappop(heap)
            for ni, nj in [[i, j-1], [i-1, j], [i, j+1], [i+1, j]]:
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                # Can go without any change.
                if c + 1 >= grid[ni][nj]:
                    if cost[ni][nj] <= c + 1:
                        continue
                    cost[ni][nj] = c + 1
                    heappush(heap, [c+1, s+1, ni, nj])
                else:
                    gg = grid[ni][nj] + (s&1 == grid[ni][nj]&1)
                    cc = max(gg, c + 1)
                    if cost[ni][nj] <= cc:
                        continue
                    cost[ni][nj] = cc
                    heappush(heap, [cc, s+1, ni, nj])
        
        return cost[-1][-1] if cost[-1][-1] < inf else -1
