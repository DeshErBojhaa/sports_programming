from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        
        dp = [float('inf')] * n
        
        ln = 0
        for v in nums:
            ind_in_dp = bisect_left(dp, v)
            dp[ind_in_dp] = v
            
            if ind_in_dp == ln:
                ln += 1
        
        return ln
