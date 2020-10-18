# 743. Network Delay Time
from queue import PriorityQueue
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        pq = PriorityQueue()
        dist = [float('inf')] * (N + 1)
        g = defaultdict(list)
        
        for f, t, cost in times:
            g[f].append(tuple([t, cost]))
        
        pq.put((0, K))
        dist[K] = 0
        
        while pq.qsize():
            cost, cur = pq.get()
            for n, c in g[cur]:
                if dist[n] > cost + c:
                    dist[n] = cost + c
                    pq.put((dist[n], n))
        
        ans = max(dist[1:])
        print(dist)
        return -1 if ans == float('inf') else ans
