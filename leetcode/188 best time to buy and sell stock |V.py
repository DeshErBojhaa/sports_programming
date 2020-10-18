class Solution:
    def maxProfit(self, K: int, p: List[int]) -> int:
        if not p or not K:
            return 0
        n = len(p)
        if K > n//2:
            return sum(max(0, p[i] - p[i-1]) for i in range(1, n))
        
        dp = [[0] * n for _ in range(K+1)]
        for k in range(1, K+1):
            max_pref_sum = float('-inf')
            # 3 2 6 5 0 3
            for i in range(1, n):
                # The inner loop can be replaced with max prefix sum.
                max_pref_sum = max(max_pref_sum, dp[k-1][i-1] - p[i-1])
                dp[k][i] = max(dp[k][i-1], p[i] + max_pref_sum)
        # for x in dp:
            # print(x)
        return dp[-1][-1]
