# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a, b = set(), set()
        both, alice, bob = [], [],[]
        para, parb = list(range(1, n+1)), list(range(1,n+1))
        para = [0] + para
        parb = [0] + parb
        ranka, rankb = [0] * (n+1), [0] *  (n+1)
        
        def find_parent(a, p):
            while p[a] != a:
                a = p[a]
            return a
        
        def join(a,b, p, r):
            a = find_parent(a, p)
            b = find_parent(b, p)
            if r[a] < r[b]:
                a, b = b, a
            p[b] = a
            r[a] += r[a] == r[b]
        
        for t, f, to in edges:
            if t == 3:
                both.append((f,to))
            elif t == 2:
                bob.append((f,to))
            else:
                alice.append((f,to))
        
        edge_count = 0
        for f,t in both:
            if find_parent(f, para) == find_parent(t, para) and find_parent(f, parb) == find_parent(t, parb):
                edge_count += 1
                continue
            
            join(f,t,para, ranka)
            join(f,t,parb, rankb)
            
        
        for f, t in alice:
            if find_parent(f, para) == find_parent(t, para):
                edge_count += 1
                continue
            join(f,t,para, ranka)
        
        for f, t in bob:
            if find_parent(f,parb) == find_parent(t, parb):
                edge_count += 1
                continue
            join(f,t,parb, rankb)
        
        for i in range(1, n+1):
            if find_parent(i, para) != find_parent(1, para):
                return -1
            if find_parent(i, parb) != find_parent(1, parb):
                return -1
        return edge_count
        
