class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        parent = list(range(n))

        def find_par(x):
            if parent[x] != x:
                parent[x] = find_par(parent[x])
            return parent[x]
        
        def join(a, b):
            pa, pb = find_par(a), find_par(b)
            if pa == pb:
                return
            parent[pa] = pb

        seen_x, seen_y = dict(), dict()
        for i, (x, y) in enumerate(points):
            if x not in seen_x:
                seen_x[x] = i
            join(seen_x[x], i)

            if y not in seen_y:
                seen_y[y] = i
            join(seen_y[y], i)

        return 1 + sum(count for _, count in Counter(find_par(i) for i in range(n)).most_common(2))
