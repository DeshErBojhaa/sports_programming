
from collections import Counter, defaultdict
from queue import PriorityQueue
class FreqStack:

    def __init__(self):
        self.c = Counter()
        self.g = defaultdict(list)
        self.N = 0

    def push(self, x: int) -> None:
        self.c[x] += 1
        self.N = max(self.N, self.c[x])
        self.g[self.c[x]].append(x)

    def pop(self) -> int:
        val = self.g[self.N].pop()
        self.c[val] -= 1
        if not self.g[self.N]:
            self.N -= 1
        return val
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
