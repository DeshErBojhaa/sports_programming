class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        N = len(nums)
        kadane = [0] * N
        kadane[0] = max(0, nums[0])
        
        
        for i, v in enumerate(nums[1:], 1):
            kadane[i] = max(max(0, kadane[i-1]) + v, 0)
        
        ans = max(kadane)
        
        for i in range(N):
            nums[i] *= -1
        
        kadane = [0] * N
        kadane[0] = max(0, nums[0])
        
        for i, v in enumerate(nums[1:], 1):
            kadane[i] = max(max(0, kadane[i-1]) + v, 0)
        
        ans2 = max(kadane)
        
        return max(ans, ans2)
