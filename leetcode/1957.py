class Solution:
    def makeFancyString(self, s: str) -> str:
        a = []
        for ch in s:
            if len(a) > 1 and ch == a[-1] and ch == a[-2]:
                continue
            a.append(ch)
        return ''.join(a)
