# 886. Possible Bipartition
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        color = {}
        g = defaultdict(list)
        
        def rec(cur, col):
            if cur in color:
                return color[cur] == col
            
            color[cur] = col
            return all(rec(nxt, 1- col) for nxt in g[cur])
        
        for d in dislikes:
            g[d[0]].append(d[1])
            g[d[1]].append(d[0])
        
        ans = True
        for i in range(1, N+1):
            if i not in color:
                ans &= rec(i, 0)
        return ans
