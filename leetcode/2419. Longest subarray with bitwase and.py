class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m, ans, tmp = max(nums), 1, 0
        for v in nums:
            if v != m:
                ans = max(ans, tmp)
                tmp = 0
                continue
            tmp += 1
        ans = max(ans, tmp)
        
        return ans