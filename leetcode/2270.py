class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        a = list(accumulate(nums))
        b = list(accumulate(nums[::-1]))[::-1]

        return sum([a[i] >= b[i+1] for i in range(len(a)-1)])
