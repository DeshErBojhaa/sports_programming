# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
from itertools import accumulate
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        sumhash, dp = {0:-1}, [float('inf')] * N
        
        ans = float('inf')
        for i, v in enumerate(accumulate(arr)):
            prev = v - target
            ln = float('inf')
            if prev in sumhash:
                prev_ind = sumhash[prev]
                ln = i - prev_ind
                
                ans = min(ans, ln + (dp[prev_ind] if prev_ind >= 0 else float('inf')))
    
            sumhash[v] = i
            dp[i] = min(ln, (dp[i-1] if i > 0 else float('inf')))
        
        return ans if ans < float('inf') else -1
