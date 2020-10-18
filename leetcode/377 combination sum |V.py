from functools import lru_cache
class Solution:
    def combinationSum4(self, n: List[int], t: int) -> int:
        dp = [0] * (t+1)
        dp[0] = 1
        
        for i in range(1, t+1):
            for x in n:
                if i -x < 0:
                    continue
                dp[i] += dp[i - x]
        return dp[t]
