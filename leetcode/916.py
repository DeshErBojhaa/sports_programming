class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        C = [Counter(a) for a in A]
        dd = defaultdict(lambda: -inf)
        for b in B:
            c = Counter(b)
            for ch, v in c.items():
                dd[ch] = max(dd[ch], v)
        B = Counter()
        for ch, v in dd.items():
            B[ch] = v
        # print(B)
        return [x for i, x in enumerate(A)  if not B - C[i]]
