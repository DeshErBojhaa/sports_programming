class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        iv = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        for i, v in enumerate(iv[1:], 1):
            if v[0] < iv[i-1][1]:
                return False
        return True
