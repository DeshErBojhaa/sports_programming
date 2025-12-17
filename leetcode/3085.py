class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        # print(c)
        c = sorted(c.values())
        # print(c)
        @cache
        def rec(a, b):
            if a == b:
                return 0
            if c[b] - c[a] <= k:
                return 0
            ans = rec(a + 1, b) + c[a]
            ans = min(ans, rec(a, b-1) + c[b] - c[a] - k)
            return ans
        return rec(0, len(c) - 1)
