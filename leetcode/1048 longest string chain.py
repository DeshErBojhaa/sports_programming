class Solution:
    def longestStrChain(self, w: List[str]) -> int:
        w = set(w)
        graph = {}
        
        for wr in w:
            graph[wr] = []
            for i in range(1, len(wr)+1):
                nw = wr[0:i-1]+wr[i:len(wr)]
                if nw in w:
                    graph[wr].append(nw)
        
        def rec(ww):
            if not graph[ww]:
                return 1
            a = 0
            for nxt in graph[ww]:
                a = max(a, rec(nxt)+1)
            return a
        
        ans = 1
        for wr in w:
            ans = max(ans, rec(wr))
        return ans
