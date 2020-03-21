from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, c: List[List[int]]) -> List[List[int]]:
        ans = []
        t = 0
        disco_time, backedge_time = {}, {}
        con = defaultdict(list)
        
        def rec(cur, par):
            nonlocal t
            t += 1
            disco_time[cur] = backedge_time[cur] = t
            
            for nxt in con[cur]:
                if nxt == par:
                    continue
                if nxt in disco_time:
                    backedge_time[cur] = min(backedge_time[cur], disco_time[nxt])
                    continue
                rec(nxt, cur)
                backedge_time[cur] = min(backedge_time[cur], backedge_time[nxt])

                if disco_time[cur] < backedge_time[nxt]:
                    ans.append((cur, nxt))
        
        for a, b in c:
            con[a].append(b)
            con[b].append(a)
        
        for i in range(n):
            if i not in disco_time:
                rec(i, i)
        return ans
