class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(cur, sm):
            if cur == len(nums):
                return int(sm == target)
            
            ans = rec(cur + 1, sm + nums[cur])
            ans += rec(cur + 1, sm - nums[cur])

            return ans
            
        return rec(0, 0)
