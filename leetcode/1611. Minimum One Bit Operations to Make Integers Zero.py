# 1611. Minimum One Bit Operations to Make Integers Zero
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        dp = {0:0}
        def rec(n):
            if n in dp:
                return dp[n]
            p = 1
            while (p << 1) <= n:
                p <<= 1
            
            # 1XXXXX -> rec(1XXXXX ^ 110000) + 1 (to convert 110000 to 10000) + pow(2, log(n) + 1) - 1
            dp[n] = rec(n ^ p ^ (p >> 1)) + 1 + p -1
            
            return dp[n]
        
        return rec(n)
