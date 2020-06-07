# 1411. Number of Ways to Paint N × 3 Grid
from functools import lru_cache
class Solution:
    def numOfWays(self, n: int) -> int:
        pattern121, pattern123, mod = 6, 6, 10**9 + 7
        for i in range(n-1):
            pattern121, pattern123 = 3 * pattern121 + 2 * pattern123, 2 * pattern121 + 2 * pattern123
            if pattern121 >= mod:
                pattern121 -= mod
            
            if pattern123 >= mod:
                pattern123 -= mod
        
        return (pattern121 + pattern123) % mod
