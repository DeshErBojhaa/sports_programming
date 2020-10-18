from collections import Counter, defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        agg = sorted([(t,n,w) for t, n, w in zip(timestamp, username, website)], key=lambda x: x[0])
        vis = defaultdict(list)
        cnt = Counter()
        for t, n, w in agg:
            vis[n].append(w)
        
        # print(vis)
        for n in set(username):
            s = set()
            if len(vis[n]) < 3:
                continue
            for i in range(len(vis[n])):
                for j in range(i+1, len(vis[n])):
                    for k in range(j+1, len(vis[n])):
                        t = tuple([vis[n][i], vis[n][j], vis[n][k]])
                        if t in s:
                            continue
                        cnt[t] -= 1
                        s.add(t)
       #     print(s)
        
        # print(cnt)
        ans = sorted((v,k) for k,v in cnt.items())
        # print(ans)
        return ans[0][1]
