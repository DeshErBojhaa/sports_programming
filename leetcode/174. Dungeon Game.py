# 174. Dungeon Game
class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        N, M = len(d), len(d[0])
        dp = [[float('inf')] * (M+1) for _ in range(N+1)]
        
        dp[N-1][M] = dp[N][M-1] = 1
        
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - d[i][j])
        
        return dp[0][0]
        
        
