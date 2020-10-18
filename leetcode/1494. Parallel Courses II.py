# 1494. Parallel Courses II
class Solution:
    def minNumberOfSemesters(self, n: int, dep: List[List[int]], k: int) -> int:
        indeg, g = [0] * n, collections.defaultdict(list)
        for a, b in dep:
            indeg[b-1] += 1
            g[a-1].append(b-1)
    
        @lru_cache(None)
        def rec(mask):
            nonlocal n
            if not mask:
                return 0
            
            candidates, ind = [], indeg[::]
            for i in range(n):
                if mask & (1<<i):
                    continue
                for nxt in g[i]:
                    ind[nxt] = max(0, ind[nxt]-1)
            

            for cur in range(n):        
                if mask&(1<<cur) and ind[cur] == 0:
                    candidates.append(cur)
                    
            canlen = len(candidates)
            ans = 100
            for nxt in itertools.combinations(candidates, min(canlen, k)):
                new_mask = mask
                for nn in nxt:
                    new_mask ^= (1<<nn)
                ans = min(ans, rec(new_mask) + 1)
            return ans
        
        return rec((1<<n)-1)
