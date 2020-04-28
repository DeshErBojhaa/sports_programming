from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        g = defaultdict(list)
        seen = set()
        
        for b, e in edges:
            g[b].append(e)
            g[e].append(b)
        
        
        def trav(cur, prev= -1):
            if cur in seen:
                return -10000
            seen.add(cur)
            ret = 1
            for nxt in g[cur]:
                if nxt == prev:
                    continue
                ret += trav(nxt, cur)
            return ret

        return trav(0) == n
