class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = nums[0]
        for i in range(1, len(nums)):
            if last & 1 == nums[i] & 1:
                return False
            last = nums[i]
        return True
