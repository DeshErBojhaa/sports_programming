class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        gg = [[] for _ in range(N)]
        loop = []

        for i, g in enumerate(graph):
            for v in g:
                gg[v].append(i)
                if v == i:
                    loop.append(i)
        
        seen, dq = [False] * N, deque()
        component = defaultdict(list)
        cid = 0

        def rec1(cur):
            seen[cur] = True
            for x in graph[cur]:
                if seen[x]:
                    continue
                rec1(x)
            dq.append(cur)
        
        def rec2(cur):
            seen[cur] = True
            component[cid].append(cur)
            for x in gg[cur]:
                if seen[x]:
                    continue
                rec2(x)
        
        for x in range(N):
            if seen[x]:
                continue
            rec1(x)
        
        seen = [False] * N
        
        while dq:
            x = dq.pop()
            if seen[x]:
                continue
            rec2(x)
            cid += 1
        
        ans, seen = [], [False] * N
        def flood(x):
            seen[x] = True
            for n in gg[x]:
                if seen[n]:
                    continue
                flood(n)
        
        for i, l in component.items():
            if len(l) <= 1:
                continue
            for x in l:
                if seen[x]:
                    continue
                flood(x)
        
        for x in loop:
            if seen[x]:
                continue
            flood(x)
        
        ans = []
        for i in range(N):
            if seen[i]:
                continue
            ans.append(i)
        return ans

