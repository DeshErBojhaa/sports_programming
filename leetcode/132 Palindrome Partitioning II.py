# 132. Palindrome Partitioning II
from functools import lru_cache
class Solution:
    def minCut(self, s: str) -> int:
        
        @lru_cache(maxsize=None)
        def rec(ss):
            if not ss:
                return 0
            
            ans = float('inf')
            for i in range(len(ss)):
                if ss[:i+1] == ss[:i+1][::-1]:
                    ans = min(ans, rec(ss[i+1:]) + 1)
            return ans
        
        return rec(s) - 1
