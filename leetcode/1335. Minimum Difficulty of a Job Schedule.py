# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        mx = jd[:]
        N = len(jd)
        if d > N:
            return -1
        
        for i in range(N-2, -1, -1):
            mx[i] = max(mx[i], mx[i+1])
        
        @lru_cache(None)
        def rec(cur, rem_d):
            if cur == N:
                return inf
            
            if rem_d == 0:
                return mx[cur]
            
            local_max, ans = -inf, inf
            for i in range(cur, N):
                local_max = max(local_max, jd[i])
                ans = min(ans, rec(i+1, rem_d-1) + local_max)
            
            return ans
        
        ans = rec(0, d-1)
        return ans if isfinite(ans) else -1
