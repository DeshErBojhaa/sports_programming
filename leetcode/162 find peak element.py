class Solution:
    def findPeakElement(self, n: List[int]) -> int:
        lo, hi = 0, len(n) -1
        while lo < hi:
            mid = (lo + hi) // 2
            if n[mid] > n[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
