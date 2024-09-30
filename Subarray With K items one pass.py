class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c, l = Counter(), 0
        ans, cum = 0, 0

        for i, n in enumerate(nums):
            c[n] += 1
            while len(c) > k:
                cum = 0
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1

            if len(c) == k:
                while c[nums[l]] > 1:
                    c[nums[l]] -= 1
                    if c[nums[l]] == 0:
                        del c[nums[l]]
                    cum += 1
                    l += 1
                ans += cum + 1

        return ans
