class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def sub_take(take):
            l, c, ans = 0, Counter(), 0
            for i, n in enumerate(nums):
                c[n] += 1
                while len(c) > take:
                    c[nums[l]] -= 1
                    if c[nums[l]] == 0:
                        del c[nums[l]]
                    l += 1
                
                ans += i - l + 1
            return ans

        return sub_take(k) - sub_take(k - 1)
