# 759. Employee Free Time
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from collections import Counter
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        linear_timeline = []
        
        for sch in schedule:
            for interval in sch:
                linear_timeline.append((interval.start, 0))
                linear_timeline.append((interval.end, 1))
        
        linear_timeline.sort()
        
        active_employee, last_end = 0, None
        ans = []
        
        for tm in linear_timeline:
            if active_employee == 0 and last_end is not None:
                if not tm[1]:
                    ans.append(Interval(last_end, tm[0]))
            if tm[1]:
                last_end = tm[0]
            active_employee += -1 if tm[1] else 1
            
        return ans
