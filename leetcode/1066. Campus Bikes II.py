# 1066. Campus Bikes II
from functools import lru_cache
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        Nw, Nb = len(workers), len(bikes)
        
        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        
        @lru_cache(maxsize=None)
        def rec(mw, bike_ind):
            if mw == 0:
                return 0
            if bike_ind == Nb:
                return float('inf')
            
            ans = float('inf')
            for i in range(Nw):
                if mw & (1 << i) != 0:
                    ans = min(ans, rec(mw ^ (1<<i), bike_ind + 1) + dist(i, bike_ind))
                    ans = min(ans, rec(mw, bike_ind + 1))
            
            return ans

        return rec((2 ** Nw)-1, 0)
