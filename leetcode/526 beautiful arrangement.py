def countArrangement(self, N: int) -> int:
        dp = [[-1] * 65536 for _ in range(16)]        
        def rec(cur, mask):
            if cur == N+1:
                return 1
                
            nonlocal dp
            if dp[cur][mask] > -1:
                # pass
                return dp[cur][mask]
            dp[cur][mask] = 0
            
            for i in range(1, N+1):
                if mask & (1 << i):
                    continue
                if cur%i and i%cur:
                    continue
                
                dp[cur][mask] += rec(cur+1, mask | (1<<i))
                
            
            return dp[cur][mask]
        
        return rec(1, 0)
