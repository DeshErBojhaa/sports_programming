class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            ans.append(nums[v])
        return ans
