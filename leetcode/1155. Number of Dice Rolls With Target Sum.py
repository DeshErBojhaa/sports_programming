class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        mod = int(1e9 + 7)
        for i in range(d):
            new_dp = [0] * (target+1)
            for t in range(1, target+1):
                for pipe in range(1, f+1):
                    new_dp[t] += (dp[t - pipe] if t >= pipe else 0)
                    if new_dp[t] >= mod:
                        new_dp[t] -= mod
            dp = new_dp
            
        return dp[target]
