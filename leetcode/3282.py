class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        return sum(accumulate(nums[:-1], max))
