# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, v in enumerate(edges):
            v.append(i)

        edges = sorted(edges, key=lambda x: x[2])
        # print(edges)
        par = list(range(n))
        
        def find_parent(a):
            while par[a] != a:
                a = par[a]
            return a
        
        def join(a, b):
            a = find_parent(a)
            b = find_parent(b)
            par[a] = b
        
        def kruskal(skipedge, init_cost):
            used_edges = int(init_cost > 0)
            cost = init_cost
            for v in edges:
                f, t, c, i = v
                if i == skipedge or find_parent(f) == find_parent(t):
                    continue
                join(f, t)
                used_edges += 1
                cost += c
            
            return cost if used_edges == n-1 else float('inf')
        
        mst_val = kruskal(-1, 0)
        must, optional = [], []
        
        for v in edges:
            par = list(range(n))
            f, t, c, i = v
            x = kruskal(i, 0)
            # print(f'edge {i, v}, mst {x}  min {mst_val}')
            if x > mst_val:
                must.append(i)
                continue
            
            par = list(range(n))
            join(find_parent(f), find_parent(t))
            x = kruskal(i, c)
            
            if x == mst_val:
                optional.append(i)
        
        return [must, optional]

# 5
# [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
