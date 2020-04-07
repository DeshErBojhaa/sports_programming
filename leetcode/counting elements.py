from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = 0
        for k in sorted(c):
            if not c[k+1]:
                continue
            ans += c[k]
        return ans
