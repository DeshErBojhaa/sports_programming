from collections import Counter, deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hc = 0
        self.c = Counter()
        self.times = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hc += 1
        self.c[timestamp] += 1
        
        self.times.append(timestamp)
        
        while self.times[0] + 300 <= timestamp:
            t = self.times.popleft()
            self.hc -= self.c[t]
            del self.c[t]
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.times.append(timestamp)
        
        while self.times[0] + 300 <= timestamp:
            t = self.times.popleft()
            self.hc -= self.c[t]
            del self.c[t]

        return self.hc


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
