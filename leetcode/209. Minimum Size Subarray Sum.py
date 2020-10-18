# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lo = hi = cur_sum = 0
        ans, N = float('inf'), len(nums)
        
        while hi < N:
            cur_sum += nums[hi]
            
            while cur_sum >= s and lo <= hi:
                ans = min(ans, hi - lo + 1)
                cur_sum -= nums[lo]
                lo += 1
            
            hi += 1
        
        while cur_sum >= s:
            ans = min(ans, hi - lo )
            cur_sum -= nums[lo]
            lo += 1
        
        return ans if ans < float('inf') else 0
