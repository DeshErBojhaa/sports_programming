# 1521. Find a Value of a Mysterious Function Closest to Target
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        seen = set()
        
        for v in arr:
            seen = {v} | {v&s for s in seen}
            ans = min(ans, *(abs(s-target) for s in seen))
        
        return ans
