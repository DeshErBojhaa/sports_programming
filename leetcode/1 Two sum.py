class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            rem = target - v
            if rem in d:
                return [d[rem], i]
            d[v] = i
