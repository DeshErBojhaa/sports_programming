class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        h, last, j, ans = [], max(x[1] for x in events), 0, 0
        for i in range(1, last + 1):
            while h and h[0] < i:
                heappop(h)
            while j < len(events) and events[j][0] <= i:
                heappush(h, events[j][1])
                j += 1
            if h:
                ans += 1
                heappop(h)
        return ans
