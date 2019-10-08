def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        
        for i, v in enumerate(stones):
            rows[v[0]].append(i)
            cols[v[1]].append(i)
        
        par = [-1 for _ in range(len(stones))]
        
        def trav(i, f):
            if par[i] != -1:
                return
            
            par[i] = f
            
            r, c = stones[i]
            for nxt in rows[r]:
                trav(nxt, f)
            
            for nxt in cols[c]:
                trav(nxt, f)
        
        f = 1
        for i in range(len(stones)):
            trav(i, f)
            f += 1
        
        c = Counter(par)
        return sum(x-1 for x in c.values())
        
