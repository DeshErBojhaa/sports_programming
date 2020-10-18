# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        
        
        def find(nums):
            prev, prevprev = max(nums[0], nums[1]), nums[0]
        
            for i, v in enumerate(nums[2:], 2):
                cur = max(prevprev + v, prev)
                prevprev = prev
                prev = cur

            return prev
        
        return max(find(nums[:-1][::1]), find(nums[1:][::1]))
