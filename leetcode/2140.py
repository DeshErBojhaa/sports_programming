class Solution:
    def mostPoints(self, Q: List[List[int]]) -> int:
        N = len(Q)
        @cache
        def rec(idx):
            if idx >= N:
                return 0
            ans = rec(idx + Q[idx][1] + 1) + Q[idx][0]
            ans = max(ans, rec(idx+1))
            return ans
        
        return rec(0)
