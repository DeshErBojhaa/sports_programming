class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dp = [i for i in range(n-1, -1, -1)]
        parents = {i:[i-1] for i in range(1, n)}

        @cache
        def update(cur, cost):
            if cur == 0:
                return
            # print(cur, cost, dp)
            for p in parents[cur]:
                # print('  ', cur, '->', p, cost, '->', dp[p])
                if dp[p] <= cost:
                    continue
                dp[p] = cost
                update(p, cost + 1)

        ret = []
        for a, b in queries:
            parents[b].append(a)
            dp[a] = min(dp[a], dp[b] + 1)
            # print('calling Update', a)
            update(a, dp[a] + 1)
            ret.append(dp[0])
            # print(dp)

        return ret
