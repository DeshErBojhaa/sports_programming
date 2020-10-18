# 1547. Minimum Cost to Cut a Stick
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        ln = len(cuts)
        dp = [[0] * ln for _ in range(ln)]
        
        for i in range(ln-2, -1, -1):
            for j in range(i+ 2, ln):
                dp[i][j] = min(dp[i][k]+ dp[k][j] for k in range(i+1, j))
                dp[i][j] += (cuts[j] - cuts[i])
        
        return dp[0][ln-1]
