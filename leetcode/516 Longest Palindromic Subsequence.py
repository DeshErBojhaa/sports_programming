from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        @lru_cache(maxsize=None)
        def rec(l, r):
            if l >= r:
                return int(l == r)
            
            ans = 1
            if s[l] == s[r]:
                ans = rec(l+1, r-1) + 2
            else:
                ans = max(ans, rec(l+1, r), rec(l, r-1))
            return ans
        
        return rec(0, len(s) - 1)
