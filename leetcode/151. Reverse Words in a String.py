# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()[::-1]
        return ' '.join(w)
