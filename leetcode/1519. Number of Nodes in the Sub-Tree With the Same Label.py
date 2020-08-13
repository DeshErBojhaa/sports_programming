# 1519. Number of Nodes in the Sub-Tree With the Same Label
from collections import Counter, defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        
        for f, t in edges:
            g[f].append(t)
            g[t].append(f)
        
        ans = [1] * n
        
        def trav(cur, par):
            # print(cur)
            cnt = Counter([labels[cur]])
            if not g[cur]:
                return cnt
            nonlocal ans
            
            for nxt in g[cur]:
                if nxt == par:
                    continue
                cnt += trav(nxt, cur)
            
            # print('Callback', cur, cnt)
            ans[cur] = max(ans[cur], cnt[labels[cur]])
            
            return cnt
        
        trav(0, -1)
        return ans
