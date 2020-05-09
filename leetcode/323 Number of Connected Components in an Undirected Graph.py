# 323. Number of Connected Components in an Undirected Graph
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        g = defaultdict(list)
        
        for f, t in edges:
            g[f].append(t)
            g[t].append(f)
            
        def trav(cur):
            seen.add(cur)
            for n in g[cur]:
                if n in seen:
                    continue
                trav(n)
        
        ans = 0
        
        for i in range(n):
            if i in seen:
                continue
            trav(i)
            ans += 1
        
        return ans
