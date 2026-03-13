class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, cur):
        if self.parent[cur] != cur:
            self.parent[cur] = self.find(self.parent[cur])
        return self.parent[cur]
    
    def join(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        used_edges = 0
        candidate_edges = []
        ans = inf

        for f, t, pw, must in edges:
            if not must:
                candidate_edges.append((f, t, pw))
                continue
            if not dsu.join(f, t):
                return -1
            ans = min(ans, pw)
            used_edges += 1
        
        candidate_edges.sort(key=lambda a: a[2], reverse=True)
        mn_pow = []
        for f, t, pw in candidate_edges:
            if used_edges == n - 1:
                break
            if not dsu.join(f, t):
                continue
            mn_pow.append(pw)
            used_edges += 1
        if used_edges != n - 1:
            return -1
        N = len(mn_pow)
        for i in range(0, min(N, k)):
            mn_pow[N-i-1] *= 2
        return min(ans, min(mn_pow, default=inf))
        
