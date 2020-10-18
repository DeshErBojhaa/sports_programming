# 1458. Max Dot Product of Two Subsequences
from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        @lru_cache(maxsize=None)
        def rec(inda, indb, taken):
            if inda >= N or indb >= M:
                return 0 if taken else -999999999999
            # Take a and b
            ret = rec(inda+1, indb+1, True) + (nums1[inda] * nums2[indb])
            
            ret = max(ret, rec(inda+1, indb, taken), rec(inda, indb+1, taken))
            
            return ret
        
        return rec(0, 0, False)
