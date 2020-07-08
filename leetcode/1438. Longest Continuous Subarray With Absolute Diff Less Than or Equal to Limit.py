# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, mn, mx = -1, deque(), deque()
        ans = 0
        
        for i, v in enumerate(nums):
            while mn and nums[mn[-1]] >= v:
                mn.pop()
            mn.append(i)
            
            while mx and nums[mx[-1]] <= v:
                mx.pop()
            mx.append(i)
            
            if mn[0] < mx[0]:  # Remove from min q
                while nums[mx[0]] - nums[mn[0]] > limit:
                    start = mn.popleft()
            elif mx[0] < mn[0]:  # Remove from max q
                while nums[mx[0]] - nums[mn[0]] > limit:
                    start = mx.popleft()
            
            ans = max(ans, i - start)
        
        return ans
