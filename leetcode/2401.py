class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans, l = 1, 0
        for i, v in enumerate(nums):
            for j in range(i-1, -1, -1):
                if v & nums[j]:
                    break
                
                v |= nums[j]
                ans = max(ans, i - j + 1)
        return ans
