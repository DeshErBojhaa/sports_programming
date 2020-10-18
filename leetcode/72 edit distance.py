class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n, m = len(w1), len(w2)
        if not n or not m:
            return max(n,m)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[-1][-1]
