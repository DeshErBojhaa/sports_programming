from collections import defaultdict
class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        sm = defaultdict(int)
        sm[0] = 1
        ans, tot = 0, 0
        for x in n:
            tot += x
            ans += sm[tot - k]
            sm[tot] += 1
        return ans
