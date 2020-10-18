# 1416. Restore The Array
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = (10**9) + 7
        N = len(s)
        
        @lru_cache(None)
        def rec(cur):
            # print(cur)
            if cur >= N:
                # print('Returning 1')
                return int(cur == N)
            if s[cur] == '0':
                # print('Returning 0')
                return 0
            
            ans = 0
            for i in range(cur+1, N+1):
                num = int(s[cur:i])
                # print('Num', num)
                if num > k or num < 1:
                    break
                ans += rec(i)
                if ans >= mod:
                    ans -= mod
            
            return ans
        
        return rec(0)
