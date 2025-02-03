class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def cnt(arr):
            ans, last, streak = 1, arr[0], 1
            for i in range(1, len(arr)):
                if arr[i] > last:
                    streak += 1
                else:
                    ans = max(ans, streak)
                    streak = 1
                last = arr[i]
            return max(ans, streak)
        
        return max(cnt(nums), cnt(nums[::-1]))
