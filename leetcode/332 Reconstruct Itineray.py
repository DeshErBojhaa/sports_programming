from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        N = len(tickets)
        g = defaultdict(list)
        
        for f, t in tickets:
            g[f].append(t)
        
        for _, v in g.items():
            v.sort(reverse=True)
        
        def dfs(cur):
            nxt = g[cur]
            while nxt:
                dfs(nxt.pop())
            ans.append(cur)
        
        dfs('JFK')
        return ans[::-1]
