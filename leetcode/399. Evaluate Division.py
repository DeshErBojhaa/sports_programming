# 399. Evaluate Division
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for eq, v in zip(equations, values):
            g[eq[0]].append((eq[1], v))
            g[eq[1]].append((eq[0], 1./v))
        
        
        def search(st, ed):
            q = deque([(st, 1.)])
            if st not in g or ed not in g:
                return -1.
            seen = {st}
            
            while q:
                cur, val = q.popleft()
                # print(cur, val)
                if cur == ed:
                    return val
                for nxt in g[cur]:
                    if nxt[0] in seen:
                        continue
                    q.append((nxt[0], val * nxt[1]))
                    seen.add(nxt[0])
                    if nxt[0] == ed:
                        return val * nxt[1]
            return -1.
        
        return [search(x[0], x[1]) for x in queries]
