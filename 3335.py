class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = Counter([ord(x) - ord('a') for x in s])
        cur, prev = [0] * 26, [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            cur[idx] += 1
        mod = int(10**9+7)
        for _ in range(t):
            cur, prev = prev, cur
            for i in range(25):
                cur[i+1] += prev[i]
                prev[i] = 0
            cur[0] += prev[-1]
            cur[1] += prev[-1]
            prev[-1] = 0
            for i in range(26):
                cur[i] %= mod
        return sum(cur) % mod
