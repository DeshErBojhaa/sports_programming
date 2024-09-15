class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [-float('inf')] * 4
        for num in b:
            for j in range(3, -1, -1):
                if j == 0:
                    dp[j] = max(dp[j], a[j] * num)
                else:
                    dp[j] = max(dp[j], dp[j-1] + a[j] * num)
        
        return dp[-1]
