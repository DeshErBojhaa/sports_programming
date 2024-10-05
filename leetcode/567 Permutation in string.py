class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c, cc = Counter(s1), Counter()
        start = 0
        for i, ch in enumerate(s2):
            if ch not in c:
                cc.clear()
                start = i + 1
                continue
            cc[ch] += 1
            if cc == c:
                return True
            while cc[ch] > c[ch]:
                cc[s2[start]] -= 1
                start += 1
        return False
