from heapq import heappush, heappop, heapify
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        debug = []
        ans = 0
        while c:
            tasks = c.most_common(n+1)
            tasks.sort()
            
            for v in tasks:
                debug.append(v[0])
                c[v[0]] -= 1
                if c[v[0]] == 0:
                    del c[v[0]]
                
            debug.extend('-' * (n - len(tasks) + 1))
        debug = ''.join(debug)
        debug = debug.rstrip('-')
        return len(debug)
