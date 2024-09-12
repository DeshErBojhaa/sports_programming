class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def rec(a, b):
            if b == len(t):
                return 1
            if a == len(s) or b == len(t):
                return 0
            
            ans = rec(a+1, b)
            if s[a] == t[b]:
                ans += rec(a+1, b+1)
            
            return ans
        
        return rec(0, 0)
