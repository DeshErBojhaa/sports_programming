def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[10000000]*n for _ in range(n)]
        
        def rec(i, j):
            if j < 0 or j >= n:
                return 100000
            if i == n:
                return 0
            nonlocal dp
            if dp[i][j] < 10000000:
                return dp[i][j]
            
            for x in range(-1,2):
                dp[i][j] = min(dp[i][j], rec(i+1, j+x) + A[i][j])
            return dp[i][j]
        
        ans = 1000000
        for j in range(n):
            ans = min(ans, rec(0,j))
        return ans
        
