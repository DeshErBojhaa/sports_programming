class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        lw, hi = int(low), int(high)
        counter = [0, 1, None, None, None, None, 9, None, 8, 6]
        
        def rec(l, r, SM, first):
            if l > r:
                # print(l, r, SM)
                return lw <= SM <= hi
            nums = [1, 6, 8, 9, 0]
            if first and l < r:
                nums.pop()
            ans = 0
            for n in nums:
                sm = SM
                if l == r and (n == 6 or n == 9):
                    continue
                sm += (pow(10, r) * counter[n])
                if l < r:
                    sm += (pow(10, l) * n)
                ans += rec(l + 1, r - 1, sm, False)
            return ans
        
        ans = 0
        for ln in range(len(low), len(high) + 1):
            # print("Len", ln, "   *** *** ***")
            ans += rec(0, ln-1, 0, True)

        return ans
