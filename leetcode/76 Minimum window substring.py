from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return s[0]
        ds, dt, sx = {}, Counter(t), Counter(s)
        if any(sx.get(k, 0) < dt[k] for k in dt):
            return ''
        l, r, ans = 0, 0, s
        
        while l <= r and r <= len(s):
            reduced = False
            while all(ds.get(k,0) >= dt[k] for k in dt) and ds:
                if len(ans) > len(s[l:r]):
                    ans = s[l:r]
                ds[s[l]] = ds[s[l]] - 1
                l += 1
                reduced = True
            
            if r == len(s) and not reduced:
                break

            if r < len(s):
                ds[s[r]] = ds.get(s[r], 0) + 1
                r += 1
            
        return ans
