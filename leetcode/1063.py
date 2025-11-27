class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack, ans = [], 0
        for i, x in enumerate(nums):
            while stack and stack[-1][0] > x:
                _, idx = stack.pop()
                ans += i - idx
            stack.append([x, i])
        n = len(nums)
        while stack:
            _, idx = stack.pop()
            ans += (n - idx)
        return ans
