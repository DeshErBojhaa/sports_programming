# 1462. Course Schedule IV
class Solution:
    def checkIfPrerequisite(self, n: int, pr: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(set)
        dist = [[math.inf] * n for _ in range(n)]
        
        for f, t in pr:
            g[f].add(t)
            dist[f][t] = 1
        
        
        ans = [False] * len(queries)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] > 100 or dist[k][j] > 100:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        for i, (f, t) in enumerate(queries):
            ans[i] = dist[f][t] < 200
        
        return ans
