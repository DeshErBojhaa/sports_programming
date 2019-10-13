def dieSimulator(self, n: int, rm: List[int]) -> int:
        mod = 10**9+7
        dp = [[[0 for _ in range(16)] for _ in range(7)] for _ in range(n+2)]
        # dp[current][last dice][consecutive] = 
        for i in range(1, 7):
            dp[1][i][1] = 1
        
        for i in range(2, n+1):
            for j in range(1, 7):
                for x in range(1, 7):
                    if x == j:
                        continue
                    for t in range(1, rm[x-1]+1):
                        dp[i][j][1] = (dp[i][j][1] + dp[i-1][x][t])%mod
                for k in range(2, rm[j-1]+1):
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1])%mod
        
        ans = 0
        for i in range(1, 7):
            for j in range(1, rm[i-1]+1):
                ans = (ans + dp[n][i][j])%mod
        return ans
