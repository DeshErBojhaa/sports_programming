from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        lo1, lo2, ans = 0, 0, 0
        d1, d2 = defaultdict(int), defaultdict(int)

        for x in A:
            d1[x] += 1
            d2[x] += 1

            while len(d1) > k:
                d1[A[lo1]] -= 1
                if not d1[A[lo1]]:
                    del d1[A[lo1]]
                lo1 += 1

            while len(d2) >= k:
                d2[A[lo2]] -= 1
                if not d2[A[lo2]]:
                    del d2[A[lo2]]
                lo2 += 1

            ans += lo2 - lo1
            
        return ans
