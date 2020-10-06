# 1024. Video Stitching
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        dp = [inf] * max(T + 1, max(x[1] for x in clips) + 1)
        dp[0] = 0
        
        for l, r in clips:
            for i in range(l, r+1):
                dp[i] = min(dp[i], dp[l] + 1)
        
        return dp[T] if isfinite(dp[T]) else -1
