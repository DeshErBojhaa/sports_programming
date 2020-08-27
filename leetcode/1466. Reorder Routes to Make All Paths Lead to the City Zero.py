# 1466. Reorder Routes to Make All Paths Lead to the City Zero
class Solution:
    def minReorder(self, n: int, conn: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        
        for a, b in conn:
            g[a].append(b)
            g[b].append(-a)
        
        def dfs(cur, par):
            cnt = 0
            for nxt in g[cur]:
                if abs(nxt) == par:
                    continue
                cnt += dfs(abs(nxt), cur) + int(nxt > 0)
            return cnt
                
        return dfs(0, -1)
