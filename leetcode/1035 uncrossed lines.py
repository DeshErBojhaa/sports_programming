def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[-1]*501 for _ in range(502)]
        
        def rec(i, j):
            if i == len(A) or j == len(B):
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            dp[i][j] = 0
            
            if A[i] == B[j]:
                dp[i][j] = rec(i+1, j+1) + 1
            
            dp[i][j] = max(dp[i][j], rec(i+1, j))
            dp[i][j] = max(dp[i][j], rec(i, j+1))
            
            return dp[i][j]
        
        return rec(0, 0)
