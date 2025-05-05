class Solution:
    def numTilings(self, n: int) -> int:
        mod = int(10**9+7)

        @cache
        def rec(cur, flag):
            if cur == n and flag == 0:
                return 1
            if cur >= n:
                return 0
            
            cnt = 0
            if flag == 0:
                cnt += rec(cur + 1, 0) # |
                cnt += rec(cur + 1, 1) # |-
                cnt += rec(cur + 1, 2) # L
                cnt += rec(cur + 2, 0)
                cnt %= mod
            elif flag == 1 or flag == 2:
                cnt += rec(cur + 2, 0)
                cnt += rec(cur + 1, 2)
                cnt %= mod
            
            return cnt % mod
        
        return rec(0, 0)
            
