class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        mx, ans = max(s), 0
        for x in sorted(s):
            tmp = 0
            while x <= mx and x in s:
                x = x * x
                tmp += 1
            ans = max(ans, tmp)
        return ans if ans > 1 else -1
