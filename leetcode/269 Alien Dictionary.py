from collections import deque, Counter, defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        indeg = Counter({c:0 for w in words for c in w})
        
        g = defaultdict(set)
        
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in g[c1]:
                        g[c1].add(c2)
                        indeg[c2] += 1
                    break
            else:
                if len(w2) < len(w1):
                    return ""
        
        ans = []
        q = deque([k for k, v in indeg.items() if not v])

        while q:
            c = q.popleft()
            ans.append(c)
            for nxt in g[c]:
                print(nxt, indeg[nxt])
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        
        if any(indeg.values()):
            return ""
        return ''.join(ans)
