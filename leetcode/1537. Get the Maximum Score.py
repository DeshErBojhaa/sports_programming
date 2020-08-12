# 1537. Get the Maximum Score
from functools import lru_cache
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = {v:i for i, v in enumerate(nums1)}
        d2 = {v:i for i, v in enumerate(nums2)}
        N1, N2 = len(nums1), len(nums2)
        arr = [nums1, nums2]
        d = [d1, d2]
        mod = (10**9) + 7
        
        @lru_cache(maxsize=None)
        def rec(cur, which):
            if which == 0 and cur >= N1:
                return 0
            if which == 1 and cur >= N2:
                return 0
            
            num = arr[which][cur]
            ans = rec(cur+1, which)
    
            if num in d[1-which]:
                ind = d[1-which][num]
                ans = max(ans, rec(ind + 1, 1- which))
                
            ans += num
            
            return ans
        
        ans = max(rec(0, 0), rec(0, 1))%mod
        return ans 
        
        
