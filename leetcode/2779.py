class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums, n = [n + k for n in nums], len(nums)
        print(nums)
        cum = [0] * (max(nums) + k + 2)
        for i, n in enumerate(nums):
            cum[n-k] += 1
            cum[n+k+1] -= 1
        cc, ans = 0, 0
        for n in cum:
            cc += n
            ans = max(ans, cc)
        return ans
