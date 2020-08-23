# 1563. Stone Game V
class Solution:
    def stoneGameV(self, vals: List[int]) -> int:
        pref = list(itertools.accumulate(vals))
        N = len(vals)
        
        def range_sum(a, b):
            if a - 1 < 0:
                return pref[b]
            return pref[b] - pref[a-1]
        
        @lru_cache(None)
        def rec(l, r):
            if l == r:
                return 0
            ans = 0
            for i in range(l, r):
                ls = range_sum(l, i)
                rs = range_sum(i+1, r)
                
                if ls >= rs:
                    ans = max(ans, rec(i+1, r) + rs)
                else rs > ls:
                    ans = max(ans, rec(l, i) + ls)
    
            return ans
        
        return rec(0, N-1)
