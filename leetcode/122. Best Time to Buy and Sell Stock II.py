class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if not p:
            return 0
        n = len(p)
        dp = [[0] * n for _ in range(2)] # dp[i][j] -> I th day with j stock in hand J can be 0/1
        for i in range(n):
            dp[1][i] = -99999
        for i in range(n):
            dp[1][i] = max((dp[1][i-1] if i else -99999), (dp[0][i-1] if i else 0) - p[i])
            dp[0][i] = max((dp[0][i-1] if i else 0), (dp[1][i-1] if i else -99999) + p[i])
            
        return max(dp[0][-1], dp[1][-1])
        
        
