# 1049. Last Stone Weight II
from functools import lru_cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def rec(cur, sm):
            if cur == len(stones):
                return sm if sm >= 0 else float('inf')
            
            return min(rec(cur+1, sm+stones[cur]), rec(cur+1, sm - stones[cur]))
        
        return rec(0, 0)
