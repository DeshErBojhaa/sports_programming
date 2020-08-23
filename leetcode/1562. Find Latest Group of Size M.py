# 1562. Find Latest Group of Size M
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N, arr = len(arr), [x-1 for x in arr]
        c = collections.Counter()
        cnt, ans = [0] * N, -2
        
        for idx, i in enumerate(arr):
            l = (cnt[i-1] if i > 0 else 0)
            r = (cnt[i+1] if i < N-1 else 0)
            
            now = l + r + 1
            
            if l:
                cnt[i-l] = now
                c[l] -= 1
            if r:
                cnt[i+r] = now
                c[r] -= 1
                
            cnt[i] = now
            c[now] += 1
            
            if c[m] > 0:
                ans = idx
        return ans + 1
