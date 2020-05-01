from collections import defaultdict
from queue import SimpleQueue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        g = defaultdict(list)
        d = defaultdict(lambda: float('inf'))
        
        for f,t,c in flights:
            g[f].append((c,t))
        
        q = SimpleQueue()
        
        q.put((src, 0, 0))  # Src, Cost, Step
        d[src] = 0
        
        while q.qsize():
            cur, cost, step = q.get()
            if step <= K:
                for c, n in g[cur]:
                    if d[n] > cost + c:
                        d[n] = cost + c
                        q.put((n, d[n], step+1))
        
        return d[dst] if d[dst] < float('inf') else -1
