# 1478. Allocate Mailboxes
from functools import lru_cache 
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        def find_distance(l, r):
            median = (l + r) // 2
            median_val = houses[median]
            ans = 0
            for i in range(l, r+1):
                ans += abs(houses[i] - median_val)
            return ans
        
        @lru_cache(maxsize=None)
        def rec(l, r, K):
            if r - l + 1 < K or K == 0 or l > r:
                return float('inf')
            if K == 1:
                d = find_distance(l, r)
                # print(f'K = 1  {l, r} dist = {d}')
                return d
            
            ans = float('inf')
            for i in range(l, r+1):
                tmp = rec(l, i, 1) + rec(i+1, r, K-1)
                ans = min(ans, tmp)
            
            return ans
        
        return rec(0, len(houses)-1, k)
