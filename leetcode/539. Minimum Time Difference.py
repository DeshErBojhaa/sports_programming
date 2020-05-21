# 539. Minimum Time Difference
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(x.split(':')[0]) * 60 + int(x.split(':')[1]) for x in timePoints]
        minutes.sort()
        
        ans = 999999999
        
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i-1], 1440 - minutes[i] + minutes[i-1])
        
        ans = min(ans, minutes[-1] - minutes[0], 1440 - minutes[-1] + minutes[0])
        return ans
