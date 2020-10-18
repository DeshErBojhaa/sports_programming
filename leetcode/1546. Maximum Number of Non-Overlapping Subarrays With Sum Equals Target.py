# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cum, found, ans = 0, {0}, 0
        
        for i, v in enumerate(nums):
            cum += v
            req = cum - target
            
            if req in found:
                ans += 1
                cum = 0
                found = {0}
            else:
                found.add(cum)
        
        return ans
