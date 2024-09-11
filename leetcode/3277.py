class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        score = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = nums[i]
            score[i][i] = nums[i]
        
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                dp[i][j] = dp[i][j-1] ^ dp[i+1][j]
        
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                score[i][j] = max(dp[i][j], score[i][j-1], score[i+1][j])
        
        ans = []
        for a, b in queries:
            ans.append(score[a][b])
        
        return ans
# 001000 | 001100 | 101000 | 111100
# 000100 | 100100 | 010100
# 100000 | 110000 |
# 010000 | 


# 000010 | 001010 | 000110 | 101110 | 010010 | 011011
# 001000 | 001100 | 101000 | 111100 | 001001 |
# 000100 | 100100 | 010100 | 110101 |
# 100000 | 110000 | 100001 |
# 010000 | 010001 |
# 000001 | 

