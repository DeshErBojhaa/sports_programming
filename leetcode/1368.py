class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        heap = []
        heappush(heap, (0, 0, 0))
        cost = [[math.inf] * M for _ in range(N)]
        cost[0][0] = 0
        
        def dir_to_index(r, c):
            d = grid[r][c]
            if d == 1:  # Right
                return r, c+1
            if d == 2:  # Left
                return r, c-1
            if d == 3:  # Low
                return r+1, c
            return r-1, c
        
        
        while heap:
            cur_cost, cur_row, cur_col = heappop(heap)
            
            if cur_row == N-1 and cur_col == M-1:
                return cur_cost
            
            for nr, nc in [(cur_row, cur_col + 1), (cur_row, cur_col - 1), (cur_row + 1, cur_col), (cur_row - 1, cur_col)]:
                if not 0 <= nr < N or not 0 <= nc < M:
                    continue
                additional = (nr, nc) != dir_to_index(cur_row, cur_col)
                if cost[nr][nc] > cur_cost + additional:
                    cost[nr][nc] = cur_cost + additional
                    heappush(heap, (cost[nr][nc], nr, nc))
        
        return cost[N-1][M-1]
