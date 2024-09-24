class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        def calc(pp, ln):
            ans = 0
            for i in range(ln):
                ans += pow(pp, i)
                if ans > n:
                    return ans
            return ans

        def ok(bin_len):
            lo, hi = 2, n

            while lo < hi:
                mid = (lo + hi) // 2
                x = calc(mid, bin_len)
                if x < n:
                    lo = mid + 1
                else:
                    hi = mid
            if calc(lo, bin_len) == n:
                return lo, lo
            return 0, lo

        ans = n - 1
        for i in range(2, 61):
            base, lo = ok(i)
            if base == lo:
                ans = min(ans, base)

        return str(ans)
