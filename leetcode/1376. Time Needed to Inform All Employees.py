# 1376. Time Needed to Inform All Employees
from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, v in enumerate(manager):
            g[v].append(i)
        
        def trav(cur):
            if not g[cur]:
                return 0
            mx = 0
            
            for nxt in g[cur]:
                mx = max(mx, trav(nxt))
            
            return mx + informTime[cur]
        
        return trav(headID)
