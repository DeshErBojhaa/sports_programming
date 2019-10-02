def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[40000000]* 1001 for _ in range(1002)]
        
        def rec(a, b):
            nonlocal dp
            if a == len(s1):
                return sum(ord(c) for c in s2[b:])
            if b == len(s2):
                return sum(ord(c) for c in s1[a:])
            
            if dp[a][b] < 20000000:
                return dp[a][b]
            
            if s1[a] == s2[b]:
                dp[a][b] = rec(a+1, b+1)
                return dp[a][b]
            
            dp[a][b] = min(dp[a][b], rec(a+1, b) + ord(s1[a]))
            dp[a][b] = min(dp[a][b], rec(a, b+1) + ord(s2[b]))
            
            return dp[a][b]
        
        return rec(0, 0)
