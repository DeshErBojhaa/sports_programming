from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def rec(si, pi):
            if si == len(s):
                return all(x == '*' for x in p[pi:])
            if si == len(s) or pi == len(p):
                return False
            
            if s[si] == p[pi] or p[pi] == '?':
                return rec(si+1, pi+1)
            
            if p[pi] == '*':
                return rec(si+1, pi) or rec(si, pi+1)
            
            return False
        
        return rec(0, 0)
