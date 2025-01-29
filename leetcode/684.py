from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        edge_ind = defaultdict(int)
        
        for i, (a,b) in enumerate(edges):
            d[a].append(b)
            d[b].append(a)
            edge_ind[(a,b)] = i+1
        
        ans = (-1,-1)
        edge_ind[ans] = 0
        visited = set()
        
        def dfs(cur, par=-1):
            if cur in visited:
                return cur
            visited.add(cur)
            
            cycle_node = -1
            for n in d[cur]:
                if n == par:
                    continue
                cycle_node = dfs(n, cur)
                if cycle_node != -1:
                    tup = (min(n,cur), max(n, cur))
                    nonlocal ans
                    if edge_ind.get(tup, -100) > edge_ind[ans]:
                        ans = tup
                    break
            
            if cycle_node == cur:
                return -1
            return cycle_node
        
        dfs(1)
        return ans
