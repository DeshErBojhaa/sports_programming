# 161. One Edit Distance
from functools import lru_cache
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        if not s:
            return len(t) == 1
        if not t:
            return len(s) == 1
        
        sN, tN = len(s), len(t)
        if abs(sN - tN) > 1:
            return False
        
        @lru_cache(maxsize=None)
        def rec(si, ti, used):
            if si == sN and ti == tN:
                return used
            if si == sN:
                return (tN - ti == 1) and used == False
            if ti == tN:
                return (sN - si == 1) and used == False
            
            if s[si] == t[ti]:
                return rec(si+1, ti+1, used)
            if used:
                return False
            
            return rec(si+1, ti, True) or rec(si, ti+1, True) or rec(si+1, ti+1, True)
        
        return rec(0, 0, False)
