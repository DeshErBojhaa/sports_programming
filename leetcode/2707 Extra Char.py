class Solution:
    def minExtraChar(self, s: str, dd: List[str]) -> int:
        N = len(s)
        @cache
        def rec(cur):
            if cur == N:
                return 0
            if cur > N:
                return inf
            ans = rec(cur+1) + 1
            for d in dd:
                if s[cur: cur+len(d)] != d:
                    continue
                ans = min(ans, rec(cur+len(d)))
            return ans
        
        return rec(0)
