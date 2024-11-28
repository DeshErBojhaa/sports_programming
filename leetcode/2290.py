class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        cost = [[inf] * M for _ in range(N)]
        heap = [[grid[0][0], 0, 0]]
        cost[0][0] = grid[0][0]
        while heap:
            c, i, j = heappop(heap)
            for ni, nj in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
                if ni < 0 or ni>= N or nj < 0 or nj >= M:
                    continue
                nc = c + grid[ni][nj]
                if nc >= cost[ni][nj]:
                    continue
                cost[ni][nj] = nc
                heappush(heap, [nc, ni, nj])
        
        return cost[-1][-1]
