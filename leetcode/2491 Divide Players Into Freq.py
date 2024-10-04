class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sm, x = sum(skill), len(skill)//2
        if sm % x:
            return -1
        each = sm // x
        c = Counter(skill)
        ans = 0
        for k, v in c.items():
            if c[k] == 0:
                continue
            rest = each - k
            if c[k] != c[rest]:
                return -1
            ans += (k * rest) * (c[k] if k != rest else c[k]//2)
            c[k] = 0
            c[rest] = 0
        return ans
