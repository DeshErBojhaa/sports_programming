from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        A, B, C = len(s1), len(s2), len(s3)
        
        if A + B != C:
            return False
        
        dp = [[False]*(B+1) for _ in range(A+1)]
        dp[0][0] = True
        
        for i in range(1, B+1):
            dp[0][i] = dp[0][i-1] and (s2[i-1] == s3[i-1])
        
        for i in range(1, A+1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
        
        for i in range(1, A+1):
            for j in range(1, B+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1]) 
        

        return dp[-1][-1]
                
