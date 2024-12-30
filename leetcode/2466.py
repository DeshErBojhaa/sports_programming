class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = (10 ** 9) + 7
        @cache
        def rec(cur):
            if cur < 0:
                return -inf
            if cur == 0:
                return 0
            
            ans = max(0, rec(cur - zero) + 1)
            ans += max(0, rec(cur - one) + 1)

            return ans % MOD
        
        
        h = max(0, rec(high))
        l = max(0, rec(low - 1))
        
        return  (h - l + MOD) % MOD
