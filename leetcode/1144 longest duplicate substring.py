class Solution:
    def longestDupSubstring(self, S: str) -> str:
        mod = 2**63
        arr = [ord(s) - ord('a') for s in S]
        N = len(S)
        def rabin_karp(l):
            h = 0
            for v in arr[:l]:
                h = (h*26 + v) % mod
            
            al = (26**l)%mod
            
            seen = {h}
            
            for i in range(1, N-l+1):
                h = ((h*26) - (al * arr[i-1]) + arr[i+l-1])%mod
                if h in seen:
                    return i
                seen.add(h)
            return -1
        
        lo, hi = 1, N
        
        while lo <= hi:
            mid = (lo+hi)//2
            start = rabin_karp(mid)
            if start != -1:
                lo = mid + 1
            else:
                hi = mid -1
        
        start = rabin_karp(lo -1)
        return S[start: start+lo-1]
