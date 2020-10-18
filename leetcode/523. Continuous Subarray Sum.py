# 523. Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        N = len(nums)
        if not k:
            for i in range(N-1):
                if nums[i] == nums[i+1] and nums[i] == 0:
                    return True
            return False
        
        cum_sum = [0] * N
        found = {nums[0]%k: 0}
        cum_sum[0] = nums[0]%k
        
        for i in range(1, N):
            cum_sum[i] = (cum_sum[i-1] + nums[i])%k
            if cum_sum[i] == 0:
                return True
            if cum_sum[i] not in found:
                found[cum_sum[i]] = i
                continue
            
            if i - found[cum_sum[i]] > 1:
                return True
        
        return False
        
