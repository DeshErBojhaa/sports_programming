class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        
        A.sort()
        lo, hi = 0, len(A) - 1
        ans = -1
        
        while lo < hi:
            sm = A[lo] + A[hi]
            if sm < K:
                ans = max(ans, sm)
                lo += 1
            else:
                hi -= 1
        return ans
