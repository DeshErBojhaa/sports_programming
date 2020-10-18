# 265. Paint House II
from functools import lru_cache
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        N, M = len(costs), len(costs[0])
        
        @lru_cache(maxsize=None)
        def rec(cur, prev_col):
            if cur == N:
                return 0
            
            ans = float('inf')
            for i in range(M):
                if i == prev_col:
                    continue
                ans = min(ans, rec(cur+1, i) + costs[cur][i])
            
            return ans
        
        return rec(0, None)
