class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[0] * M for _ in range(N)]
        for d in dp:
            d[0] = 1

        for j in range(1, M):
            for i in range(N):
                if grid[i][j-1] < grid[i][j]:
                    if dp[i][j-1]:
                        dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
                if i - 1 >= 0 and grid[i-1][j-1] < grid[i][j]:
                    if dp[i-1][j-1]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                if i + 1 < N and grid[i+1][j-1] < grid[i][j]:
                    if dp[i+1][j-1]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 1)
        
        ans = max(max(d) for d in dp)
        return max(0, ans - 1)
