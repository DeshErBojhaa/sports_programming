# 1377. Frog Position After T Seconds
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = defaultdict(set)        
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)

        vis = set()
        
        def trav(cur, tm, p=1):
            if tm <= 0:
                return 1.0/ p if cur == target else 0
            
            vis.add(cur)
            ans = 0
            
            nxt = g[cur] - vis
            if not nxt:
                return trav(cur, tm-1, p)
            
            for n in nxt:
                ans += trav(n, tm - 1, p * len(nxt))
            
            return ans
        
        return trav(1, t)
        
