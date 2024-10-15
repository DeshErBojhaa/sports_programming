class Solution:
    def minimumSteps(self, s: str) -> int:
        bidx, ans = len(s) - 1, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                continue
            ans += bidx - i
            bidx -= 1
        return ans
