class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen, ans, l, sm = set(), 0, 0, 0

        for i, n in enumerate(nums):
            while n in seen or i - l >= k:
                seen.remove(nums[l])
                sm -= nums[l]
                l += 1

            sm += n
            seen.add(n)
            if i - l == k - 1:
                ans = max(ans, sm)

        return ans
