# 368. Largest Divisible Subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        N, ans = len(nums), []
        dp = [0] * N
        
        for i in range(N):
            tmp = 0
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp + 1
            
        maxlen, ind = max([(v, i) for i, v in enumerate(dp)])
        ans = [nums[ind]]
        maxlen -= 1
        
        for i in range(ind, -1, -1):
            if dp[i] == maxlen and ans[-1]%nums[i] == 0:
                ans.append(nums[i])
                maxlen -= 1
        
        return ans
