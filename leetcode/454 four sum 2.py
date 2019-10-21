def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d1, d2 = defaultdict(int), defaultdict(int)
        
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                d1[a+b] += 1
        for i, c in enumerate(C):
            for j, d in enumerate(D):
                d2[c+d] += 1
        
        ans = 0
        for c in d1:
            ans += d1[c] * d2[-c]
        
        return ans
