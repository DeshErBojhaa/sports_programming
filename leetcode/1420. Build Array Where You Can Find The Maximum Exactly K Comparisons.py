# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = (10**9) + 7
        
        @lru_cache(None)
        def rec(cur, kk, last):
            if kk < 0:
                return 0
            if cur == n:
                return int(kk == 0)
            
            ans = 0
            for i in range(1, m+1):
                big = int(i > last)
                ans += rec(cur+1, kk - big, max(last,i))
                while ans >= mod:
                    ans -= mod
            return ans
        
        return rec(0, k, -1)
