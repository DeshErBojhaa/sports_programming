class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter([n % k for n in arr])
        for kk, v in c.items():
            if kk == 0 and v&1:
                return False
            if kk == 0:
                continue
            kkk = k - kk
            if v != c[kkk]:
                return False
        return True
