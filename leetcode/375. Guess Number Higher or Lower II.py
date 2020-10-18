# 375. Guess Number Higher or Lower II
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]* (n+1) for _ in range(n+1)]
        
        for l in range(n-1, 0, -1):
            for r in range(l+1, n+1):
                dp[l][r] = min(x + max(dp[l][x-1], dp[x+1][r]) for x in range(l, r))
        
        return dp[1][n]
