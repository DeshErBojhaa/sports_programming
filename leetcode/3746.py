class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count('a')
        b =  abs(len(s) - a)
        return abs(b - a)
