class Solution:
    def countPaths(self, NN: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b, c in roads:
            g[a].append((b, c))
            g[b].append((a, c))

        path = [inf] * NN
        path[0] = 0
        cnt = [0] * NN
        cnt[0] = 1
        q = [[0, 0]]
        def dijkstra():
            while q:
                cost, cur = heappop(q)
                for n, nc in g[cur]:
                    if cost + nc > path[n]:
                        continue
                    if cost + nc < path[n]:
                        path[n] = cost + nc
                        cnt[n] = cnt[cur]
                        heappush(q, [path[n], n])
                    else:
                        cnt[n] += cnt[cur]
                        cnt[n] %= int(1e9 + 7)

        dijkstra()
        return cnt[-1]
