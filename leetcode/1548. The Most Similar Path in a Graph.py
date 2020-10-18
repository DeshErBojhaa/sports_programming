# 1548. The Most Similar Path in a Graph
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        g = defaultdict(list)
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        
        N = len(targetPath)
        
        @lru_cache(None)
        def rec(cur, idx):
            if idx == N:
                return 0
            
            ans = math.inf
            for nxt in g[cur]:
                ans = min(ans, rec(nxt, idx + 1) + (names[nxt] != targetPath[idx]))
            
            return ans
        
        startidx, mincost = 0, math.inf
        
        for i in range(len(names)):
            ans = rec(i, 1) + (names[i] != targetPath[0])
            if ans < mincost:
                mincost = ans
                startidx = i
        
        def path(cur, idx):
            if idx == N:
                return
            for nxt in g[cur]:
                if rec(cur, idx) == rec(nxt, idx+1) + (names[nxt] != targetPath[idx]):
                    ans.append(nxt)
                    return path(nxt, idx+1)
        
        ans = [startidx]
        path(startidx, 1)
        return ans
