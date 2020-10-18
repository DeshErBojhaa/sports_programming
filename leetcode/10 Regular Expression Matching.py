from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def rec(si, pi):
            if si == -1 and pi == -1:
                return True
            if si == -1:
                while pi > 0 and p[pi] == '*':
                    pi -= 2
                return pi == -1
                
            if pi == -1:
                return False
            
            if p[pi] == '.' or s[si] == p[pi]:
                return rec(si-1, pi-1)
            if p[pi] == '*':
                zero_match = rec(si, pi-2)
                one_or_more = False
                if p[pi-1] == '.' or p[pi-1] == s[si]:
                    one_or_more = rec(si-1, pi)
                return zero_match or one_or_more
            
            if p[pi] != s[si]:
                return False

        
        
        return rec(len(s)-1, len(p)-1)
