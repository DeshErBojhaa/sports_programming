# 1326. Minimum Number of Taps to Open to Water a Garden
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = []
        for i, d in enumerate(ranges):
            if not d:
                continue
            arr.append([max(0, i-d), min(n, i+d)])
        
        arr.sort(key=lambda x: (x[0], -x[1]))
        ans, l, idx = 0, 0, 0
        N = len(arr)
        
        while idx < n:
            r = -inf
            while l < N and arr[l][0] <= idx:
                r = max(r, arr[l][1])
                l += 1
            if isinf(r):
                return -1
            
            idx = r
            ans += 1
        
        return ans
