# 416. Partition Equal Subset Sum
from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        sm = sum(nums)
        if sm%2:
            return False
        
        @lru_cache(maxsize=None)
        def rec(rem, cur):
            if not rem:
                return True
            if cur == len(nums):
                return rem == 0
            
            return rec(rem, cur+1) or rec(rem - nums[cur], cur+1)
        
        return rec(sm//2, 0)
