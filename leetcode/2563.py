class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0

        for i, v in enumerate(nums):
            idx_right = bisect_right(nums, upper - v, i + 1)
            idx_left = bisect_left(nums, lower - v, i + 1)
            ans += max(0, idx_right - idx_left)

        return ans
