from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        iv = sorted(intervals)
        q = []
        
        heappush(q, iv[0][1])
        
        for st, ed in iv[1:]:
            if st >= q[0]:
                heappop(q)
            heappush(q, ed)
        return len(q)
        
#   ----------------
#     --------
#          ----------
#            -----
