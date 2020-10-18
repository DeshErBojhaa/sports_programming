from bisect import bisect

def rec(d, c, pos, dp):
    if pos >= len(d):
        return 0
    if dp[pos] < 10000000:
        return dp[pos]
    
    # One day
    dp[pos] = c[0] + rec(d, c, pos+1, dp)
    
    # One Week
    new_pos = bisect(d, d[pos]+6)
    dp[pos] = min(dp[pos], c[1] + rec(d, c, new_pos, dp))
    
    # One Month
    new_pos = bisect(d, d[pos] + 29)
    dp[pos] = min(dp[pos], c[2] + rec(d, c, new_pos, dp))

    return dp[pos]

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [10000000] * 366
        return rec(days, costs, 0, dp)
