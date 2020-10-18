def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = defaultdict(list)
        
        for a in allowed:
            d[tuple(a[:2])].append(a[2])
        
        def make(l, c, s, ans):
            if c == len(l):
                ans.append(s)
                return
            for x in l[c]:
                make(l, c+1, s+x, ans)
        
        def rec(cs, nx=''):
            if len(cs) == 1:
                return True
            
            ll, al = [], []
            for i in range(len(cs)-1):
                l = []
                l.extend(d[tuple([cs[i],cs[i+1]])])
                ll.append(l)
            make(ll, 0, '', al)
            
            #print(al)
            for s in al:
                if rec(s):
                    return True
            return False
        return rec(bottom)   
