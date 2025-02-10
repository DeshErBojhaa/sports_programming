class Solution:
    def clearDigits(self, s: str) -> str:
        a = []
        for c in s:
            if c.isdigit():
                a.pop()
                continue
            a.append(c)
        return ''.join(a)
