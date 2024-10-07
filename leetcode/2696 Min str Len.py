class Solution:
    def minLength(self, s: str) -> int:
        for i in range(100):
            s = s.replace('AB', '')
            s = s.replace('CD', '')
        return len(s)
