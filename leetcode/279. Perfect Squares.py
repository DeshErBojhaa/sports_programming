# 279. Perfect Squares
from math import sqrt, ceil, floor
from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, ceil(sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for x in square_nums:
                if x > i:
                    break
                dp[i] = min(dp[i - x] + 1, dp[i])
        
        return dp[-1]
