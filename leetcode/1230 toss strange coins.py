def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0.0 for _ in range(1002)] for _ in range(1002)]
        # dp = [[0.0000000000]*1001 for _ in range(1001)]
        
        dp[1][0] = (1.0 - prob[0])
        dp[1][1] = prob[0]
        
        for i in range(2, n+1):
            for j in range(0, target+1):
                dp[i][j] += dp[i-1][j] * (1.0 - prob[i-1]) # Assuming this flip is 0
                if j:
                    dp[i][j] += dp[i-1][j-1] * prob[i-1]
        
        return dp[n][target]
