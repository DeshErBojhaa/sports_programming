class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def rec2(l, r):
            if l > r:
                return 0

            ans = rec2(l + 1, r) + 1
            for i in range(l + 1, r + 1):
                if s[l] == s[i]:
                    tmp = rec2(l, i - 1) + rec2(i + 1, r)
                    ans = min(ans, tmp)
            return ans

        return rec2(0, len(s) - 1)
