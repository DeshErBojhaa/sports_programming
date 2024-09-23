class Solution:
    def validSubstringCount(self, w: str, ww: str) -> int:
        c = Counter(ww)
        ans, covered = 0, False
        cc = Counter()

        def ok():
            for ch_, v in c.items():
                if cc[ch_] < v:
                    return False
            return True

        left = 0
        for i, ch in enumerate(w):
            cc[ch] += 1
            while left < i and cc[w[left]] > c[w[left]]:
                cc[w[left]] -= 1
                left += 1

            if not covered:
                covered = ok()
            if covered:
                ans += left
                ans += 1

        return ans
