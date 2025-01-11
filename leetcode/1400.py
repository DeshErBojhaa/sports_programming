class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)
        return sum(x&1 for x in c.values()) <= k and len(s) >= k
