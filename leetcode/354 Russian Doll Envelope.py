from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        env = [e[1] for e in env]
        
        dp = [float('inf')] * len(env)
        
        ln = 0
        for v in env:
            dp_ind = bisect_left(dp, v)
            dp[dp_ind] = v
            
            if dp_ind == ln:
                ln += 1
        
        return ln
