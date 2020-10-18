def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * 1001 for i in range(1002)]
        
        def rec(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if dp[i][j] > -1:
                return dp[i][j]
            dp[i][j] = 0
            
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], rec(i+1, j+1) + 1)
            
            dp[i][j] = max(dp[i][j], rec(i+1, j))
            dp[i][j] = max(dp[i][j], rec(i, j+1))
            
            return dp[i][j]
        
        ans = rec(0,0)
        return ans
