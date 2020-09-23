# 1269. Number of Ways to Stay in the Same Place After Some Steps
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrlen = min(arrLen, (steps//2)+1)
        MOD = 10 ** 9 + 7
        dp_cur, dp_nxt = [0] * (arrlen + 2), [0] * (arrlen + 2)
        dp_cur[1] = 1
        
        for _ in range(steps):
            for i in range(1, arrlen+1):
                dp_nxt[i] = (dp_cur[i] + dp_cur[i-1] + dp_cur[i+1]) % MOD
            # print(dp_nxt)
            dp_cur, dp_nxt = dp_nxt, dp_cur
        
        return dp_cur[1]
