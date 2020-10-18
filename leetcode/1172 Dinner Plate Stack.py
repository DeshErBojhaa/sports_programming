from heapq import heappush, heappop
from collections import Counter
class DinnerPlates:

    def __init__(self, capacity: int):
        self.racks = []
        self.avail_rack = 0
        self.cap = capacity
        self.last_ind = 0
        
    def push(self, val: int) -> None:
        if len(self.racks) <= self.avail_rack:
            self.racks.append([])
        
        self.racks[self.avail_rack].append(val)
        
        while self.avail_rack < len(self.racks) and len(self.racks[self.avail_rack]) == self.cap:
            self.avail_rack += 1
        self.last_ind = max(self.last_ind, len(self.racks)-1)
        
    def pop(self) -> int:
        if len(self.racks) == 0:
            return -1
        # last_ind = len(self.racks) - 1
        while self.last_ind and len(self.racks[self.last_ind]) == 0:
            self.last_ind -= 1
        # print(self.racks, self.last_ind)
        if len(self.racks[self.last_ind]) == 0:
            return -1
        
        val = self.racks[self.last_ind].pop()
        
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.racks):
            return -1
        if len(self.racks[index]) == 0:
            return -1
        val = self.racks[index].pop()
        self.avail_rack = min(self.avail_rack, index)
        
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
