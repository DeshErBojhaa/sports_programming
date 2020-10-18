# 473. Matchsticks to Square
from functools import lru_cache
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False
        total_len = sum(nums)
        N = len(nums)
        if total_len%4:
            return False
        side = total_len // 4
        if any([x > side for x in nums]):
            return False
        nums.sort()
        
        @lru_cache(maxsize=None)
        def rec(mask, cur_side):
            if cur_side > side:
                return False
            if mask == 0:
                return cur_side == side
            if cur_side == side:
                return rec(mask, 0)
            
            ans = False
            for i in range(N-1, -1, -1):
                if (mask & (1<<i)):
                    if rec(mask ^ (1<<i), cur_side + nums[i]):
                        ans = True
                        break
            return ans
        
        return rec(2**N-1, 0)
