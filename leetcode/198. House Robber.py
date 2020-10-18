class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return max(nums)
        
        prev, prevprev = max(nums[0], nums[1]), nums[0]
        
        for i, v in enumerate(nums[2:], 2):
            cur = max(prevprev + v, prev)
            prevprev = prev
            prev = cur
        
        return prev
            
