class Solution:
    def countCompleteComponents(self, n: int, eee: List[List[int]]) -> int:
        edges = defaultdict(set)
        for a, b in eee:
            edges[a].add(b)
            edges[b].add(a)

        color = [-1] * (n)
        def col(cur, cnt):
            if color[cur] != -1:
                return
            color[cur] = cnt
            for n in edges[cur]:
                if color[n] != -1:
                    continue
                col(n, cnt)
        
        _id = 0
        for i in range(n):
            if color[i] != -1:
                continue
            col(i, _id)
            _id += 1
        
        components = defaultdict(list)
        for i, c in enumerate(color):
            components[c].append(i)
        # print(color)
        ans = 0
        for comps in components.values():
            # print("comps", comps)
            ok = True
            for i in range(len(comps)):
                if not ok:
                    break
                for j in range(i+1, len(comps)):
                    if comps[i] in edges[comps[j]]:
                        continue
                    if comps[j] in edges[comps[i]]:
                        continue
                    ok = False
                    break
            ans += ok
        return ans
