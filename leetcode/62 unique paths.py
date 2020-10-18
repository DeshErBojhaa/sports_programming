dp = [[0 for x in range(101)] for y in range(101)]
        
for i in range(101):
    dp[i][0] = dp[0][i] = 1

for i in range(1,101):
    for j in range(1, 101):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return dp[m-1][n-1]
