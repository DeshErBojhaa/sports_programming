class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        cum = [0] * len(nums)
        cum[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            cum[i] = nums[i] + cum[i+1]

        sm = 0
        for i, n in enumerate(nums):
            sm += n
            
            if sm-n == (cum[i+1] if i+1 < len(nums) else 0):
                return i
        return -1
