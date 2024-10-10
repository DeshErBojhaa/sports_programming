class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        idx = sorted(list(range(n)), key=lambda x: (nums[x], x))

        mn, ans = n, 0
        for n in idx:
            mn = min(mn, n)
            ans = max(ans, n - mn)
        return ans
