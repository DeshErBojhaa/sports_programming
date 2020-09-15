# 1235. Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        N, dp = len(arr), [[0,0]]
        
        for s, e, p in arr:
            i = bisect.bisect(dp,[s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        
        return dp[-1][1]
            
