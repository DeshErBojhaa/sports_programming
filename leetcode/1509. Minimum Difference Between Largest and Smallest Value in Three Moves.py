# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
from collections import Counter
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 5:
            return 0
        nums.sort()
        ans = float('inf')
        for i in range(4):
            for j in range(0, 4):
                if i + j != 3:
                    continue
                if j == 0:
                    na = nums[i:]
                else:
                    na = nums[i:-j]
                if not na:
                    continue
                # print(na)
                ans = min(ans, max(na) - min(na))
        
        return ans
