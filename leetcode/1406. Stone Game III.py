# 1406. Stone Game III
class Solution:
    def stoneGameIII(self, sv: List[int]) -> str:
        N = len(sv)
        @lru_cache(None)
        def rec(cur):
            if cur == N:
                return 0
            if cur > N:
                return -math.inf
            
            ans = -math.inf
            
            ans = sv[cur] - rec(cur+1)
            
            if cur + 1 < N:
                ans = max(ans, -rec(cur+2) + sv[cur] + sv[cur+1])
            if cur + 2 < N:
                ans = max(ans, -rec(cur+3) + sv[cur] + sv[cur+1] + sv[cur+2])
            
            return ans
        
        ans = rec(0)
        if ans == 0:
            return 'Tie'
        if ans > 0:
            return 'Alice'
        return 'Bob'
