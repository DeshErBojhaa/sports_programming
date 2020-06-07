# 310. Minimum Height Trees
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n < 2 or not edges or not edges[0]:
            return [0]
        
        dist = defaultdict(list)
        leaf = None
        
        
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        for i in range(n):
            if len(g[i]) == 1:
                leaf = i
                break
                
        def furthest_leaf(cur, par):
            if len(g[cur]) == 1 and cur != leaf:
                return 0, cur
            farthest = 0
            node = None
            
            for n in g[cur]:
                if n == par:
                    continue
                d = furthest_leaf(n, cur)
                if d[0] + 1 > farthest:
                    farthest = d[0] + 1
                    node = d[1]
            return (farthest, node)
        
        def find_longest_path(cur, par):
            # print(cur, par)
            if len(g[cur]) == 1 and par is not None:
                # print('returning', cur)
                return [cur]
            tmp_path = []
            for n in g[cur]:
                if n == par:
                    continue
                tmp = find_longest_path(n, cur)
                if len(tmp) > len(tmp_path):
                    tmp_path = tmp[::]
            return [cur] + tmp_path
        
    
        fl = furthest_leaf(leaf, None)
        longest_path = find_longest_path(fl[1], None)
        max_dist = len(longest_path)
        ans = []
        if max_dist%2 == 0:
            ans.append(longest_path[~max_dist//2])
        
        ans.append(longest_path[max_dist//2])

        return ans
