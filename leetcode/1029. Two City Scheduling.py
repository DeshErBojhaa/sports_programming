# 1029. Two City Scheduling
from functools import lru_cache
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        
        @lru_cache(maxsize=None)
        def rec(cur, a, b):
            if cur == N:
                if not a and not b:
                    return 0
                return float('inf')
            
            return min(rec(cur+1, a-1, b)+costs[cur][0], rec(cur+1, a, b-1)+costs[cur][1])
        
        return rec(0, N//2, N//2)
