# 1060. Missing Element in Sorted Array
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i, n in enumerate(nums[:-1]):
            dis = nums[i+1] - n - 1
            if dis >= k:
                return n + k
            k -= dis
        
        return nums[-1] + k
