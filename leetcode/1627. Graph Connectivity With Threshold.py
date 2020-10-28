class Solution:
    def areConnected(self, n, threshold, queries):
        if threshold == 0:
            return [True] * len(queries)
        
        par = list(range(n+1))
        rank = [0] * (n+1)

        def find_parent(a):
            if par[a] == a:
                return a
            par[a] = find_parent(par[a])
            return par[a]


        def join(a, b):
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            par[pb] = pa
            rank[pa] += (rank[pa] == rank[pb])


        for i in range(threshold+1, n+1):
            for j in range(i, n+1, i):
                join(i, j)

        ans = [False] * len(queries)

        for i, (a,b) in enumerate(queries):
            ans[i] = find_parent(a) == find_parent(b)

        return ans


s = Solution()
ans = s.areConnected(6, 2 , [[1,4],[2,5],[3,6]])
print(ans)

from random import randint

queries = []
for i in range(1000):
    queries.append([randint(1, 10000), randint(1, 10000)])

ans = s.areConnected(10000, 2, queries)
print(ans)
print(queries)

