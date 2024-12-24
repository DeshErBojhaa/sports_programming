class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n1, n2 = len(edges1), len(edges2)
        g1, g2 = [[] for _ in range(n1+1)], [[] for _ in range(n2+1)]
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a, b in edges2:
            g2[a].append(b)
            g2[b].append(a)

        def dfs(g, cur, par, d, dist):
            d[cur] = dist
            for nxt in g[cur]:
                if nxt == par:
                    continue
                dfs(g, nxt, cur, d, dist+1)

        def min_dist(g):
            d = {}
            dfs(g, 0, -1, d, 0)
            node, node_dist = -1, -1
            for k, v in d.items():
                if v < node_dist:
                    continue
                node = k
                node_dist = v

            # print('0 -> ', node, node_dist)
            d1 = {}
            dfs(g, node, -1, d1, 0)
            node2, node2_dist = -1, -1
            for k, v in d1.items():
                if v < node2_dist:
                    continue
                node2 = k
                node2_dist = v
            # print(node, ' ->', node2, node2_dist)

            d2 = {}
            dfs(g, node2, -1, d2, 0)
            node2_dist = max(node2_dist, max(d2.values()))
            # print(d2)
            min_diameter = 10**10
            for i in range(len(g)):
                min_diameter = min(min_diameter, max(d1[i], d2[i]))

            # print('Diameter', min_diameter)
            return min_diameter, node2_dist

        min_dia1, max_dia1 = min_dist(g1)
        min_dia2, max_dia2 = min_dist(g2)
        return max(min_dia1+min_dia2+1, max(max_dia1, max_dia2))
