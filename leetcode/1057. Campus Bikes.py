# 1057. Campus Bikes
from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        assigned_workers, used_bikes = set(), set()
        
        ind = 0
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                g[dist].append((i,j))

        ans = [-1] * len(workers)
        
        for i in range(2001):
            for w, b in g[i]:
                if w in assigned_workers or b in used_bikes:
                    continue
                ans[w] = b
                assigned_workers.add(w)
                used_bikes.add(b)
        
        return ans
