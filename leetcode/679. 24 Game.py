# 679. 24 Game
from itertools import permutations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def rec(numss):
            if len(numss) == 1:
                return abs(numss[0] - 24) < 0.000001
            
            ret = False
            for a, b, *rest in permutations(numss):
                ret = ret or any(rec([x] + rest) for x in [a+b, a-b, a*b, b and a/b])
                if ret:
                    return True
            return ret
        
        return rec(nums)
