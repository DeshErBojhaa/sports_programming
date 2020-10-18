# 995. Minimum Number of K Consecutive Bit Flips
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        if K == 1:
            return A.count(0)
        
        N = len(A)
        cum, dp, ans = 0, [0] * N, 0
        
        for i, v in enumerate(A):
            if i:
                dp[i] += dp[i-1]
            if v == 0:
                if dp[i]%2 == 0:
                    if i + K > N:
                        return -1
                    dp[i] += 1
                    ans += 1
                    if i + K < N:
                        dp[i+K] -= 1
            else:
                if dp[i]%2:
                    if i + K > N:
                        return -1
                    dp[i] += 1
                    ans += 1
                    if i + K < N:
                        dp[i+K] -= 1
        
        return ans
