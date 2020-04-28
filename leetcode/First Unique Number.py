from heapq import heappush, heappop
from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.c = Counter()
        self.q = []
        self.N = 0
        
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.q and self.c[self.q[0][1]] > 1:
            heappop(self.q)
        if not self.q:
            return -1
        # val = heappop(self.q)
        return self.q[0][1]
    
    def add(self, value: int) -> None:
        self.c[value] += 1
        if self.c[value] > 1:
            return
        heappush(self.q, (self.N, value))
        self.N += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
