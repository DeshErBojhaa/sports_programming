# 1488. Avoid Flood in The City
from collections import Counter, deque
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days, rain_on_lake, N = [], {}, len(rains)
        ans = [-1] * N
        
        for day_no, lake_no in enumerate(rains):
            if lake_no == 0:
                dry_days.append(day_no)
                continue
            
            prev_rain_day = rain_on_lake.get(lake_no, -1)
            if prev_rain_day == -1:
                rain_on_lake[lake_no] = day_no
                continue
            rain_on_lake[lake_no] = day_no
            
            if len(dry_days) == 0:
                return []
            
            idx = bisect.bisect_right(dry_days, prev_rain_day)
            if idx == len(dry_days) or dry_days[idx] < prev_rain_day:
                return []
            
            ans[dry_days.pop(idx)] = lake_no
        
        while dry_days:
            ans[dry_days.pop()] = 1

        return ans
            
        
