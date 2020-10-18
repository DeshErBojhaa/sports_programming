from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.pref_sum = []
        running_sum = 0
        for v in w:
            running_sum = running_sum + v
            self.pref_sum.append(running_sum)
        self.max_sum = running_sum

    def pickIndex(self) -> int:
        val = randint(1, self.max_sum)
        lo, hi = 0, len(self.pref_sum) -1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.pref_sum[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
