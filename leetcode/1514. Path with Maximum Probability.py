# 1514. Path with Maximum Probability
from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for e, p in zip(edges, succProb):
            g[e[0]].append((e[1], p))
            g[e[1]].append((e[0], p))
        
        dist, pq = [-1.] * n, PriorityQueue()
        dist[start] = 1.
        pq.put((-1., start))
        
        while pq.qsize():
            pro, cur = pq.get()
            pro *= -1.
            for nxt, p in g[cur]:
                p_nxt = pro * p
                if dist[nxt] < p_nxt:
                    dist[nxt] = p_nxt
                    pq.put((-dist[nxt], nxt))
                
        return 0. if dist[end] < 0. else dist[end]
            
