class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        last, ans = {}, inf
        for i, x in enumerate(nums):
            _x = int(str(x)[::-1])
            dist = i - last.get(x, -inf)
            ans = min(ans, dist)
            last[_x] = i
        return ans if ans < inf else -1
