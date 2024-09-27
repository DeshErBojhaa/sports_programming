class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)
        for i, r in enumerate(ring):
            pos[r].append(i)

        @cache
        def rec(r, k):
            if k == len(key):
                return 0
            ans = inf
            ch = key[k]
            for p in pos[ch]:
                cst = (r - p + n) % n
                ans = min(ans, rec(p, k+1) + 1 + cst)
                cst = (p - r + n) % n
                ans = min(ans, rec(p, k+1) + 1 + cst)
            return ans

        return rec(0, 0)
            
