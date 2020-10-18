class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        x = sum([(-v if d else v) for d, v in shift])%len(s)
        return s[x:] + s[:x]
