# 1498. Number of Subsequences That Satisfy the Given Sum Condition
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, mod = 0, (10**9)+7
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += pow(2, r - l, mod)
                if ans >= mod:
                    ans -= mod
                l += 1
        
        return ans
