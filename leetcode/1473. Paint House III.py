# 1473. Paint House III
from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        N = len(houses)
        
        @lru_cache(maxsize=None)
        def rec(cur, prev_col, neighbour):
            if cur == N:
                return 0 if neighbour == target else float('inf')
            if neighbour > target:
                return float('inf')
            
            ans = float('inf')
            if houses[cur] == 0:
                for i in range(n):
                    ans = min(ans, rec(cur+1, i+1, neighbour + (i+1 != prev_col)) + cost[cur][i])
            else:
                ans = rec(cur+1, houses[cur], neighbour + (prev_col != houses[cur]))
            
            return ans
        
        ret = rec(0, houses[0], int(houses[0] != 0))
        return -1 if ret == float('inf') else ret
