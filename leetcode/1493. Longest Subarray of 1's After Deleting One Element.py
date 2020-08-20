# 1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = [0] * N, [0] * N
        
        l[0] = nums[0]
        
        for i in range(1, N):
            if nums[i]:
                l[i] = l[i-1] + 1
        
        r[N-1] = nums[N-1]
        
        for i in range(N-2, -1, -1):
            if nums[i]:
                r[i] += r[i+1] + 1
        
        ans = 0
        
        for i in range(N):
            ans = max(ans, (l[i-1] if i else 0) + (r[i+1] if i+1 < N else 0))
        
        return ans
        
