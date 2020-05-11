# 815. Bus Routes
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        N = len(routes)
        rout_set = [set(x) for x in routes]
        g = defaultdict(list)
        routid = 0
        rout_set_id = {i:v for i, v in enumerate(rout_set)}
        
        for i in range(N):
            for j in range(i+1, N):
                r1 = rout_set_id[i]
                r2 = rout_set_id[j]
                
                if not r1.isdisjoint(r2):
                    g[i].append(j)
                    g[j].append(i)
        
        q = deque()
        dist = {}
        for i, r in enumerate(rout_set):
            if S in r:
                q.append(i)
                dist[i] = 1
        
        while q:
            ind = q.popleft()
            rout = rout_set_id[ind]
            # print(ind, rout)
            if T in rout:
                return dist[ind]
            
            for n in g[ind]:
                if n in dist:
                    continue
                dist[n] = dist[ind] + 1
                q.append(n)
        return -1

