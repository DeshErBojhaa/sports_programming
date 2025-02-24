class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        bob_path = []
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def rec(cur, par, path):
            nonlocal bob_path
            if cur is None or bob_path:
                return
            path.append(cur)
            if cur == bob:
                bob_path = path[::-1]
                return
            
            for v in g[cur]:
                if v == par:
                    continue
                rec(v, cur, path)
            path.pop()
        
        rec(0, -1, [])
        bob_path = {a: b for b, a in enumerate(bob_path)}
        
        def rec2(cur, par, tm):
            
            now = amount[cur]
            bb = bob_path.get(cur, inf)
            if bb < tm:
                now = 0
            elif bb == tm:
                now //= 2
            mx = -inf
            for v in g[cur]:
                if v == par:
                    continue
                mx = max(mx, rec2(v, cur, tm + 1))
            
            if mx == -inf:
                mx = 0
            return mx + now
            
        return rec2(0, -1, 0)
